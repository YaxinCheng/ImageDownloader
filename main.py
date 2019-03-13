import asyncio, ClipboardReader, Downloader, URLGenerator, argparse, os, time
from Extractor import Extractor

parser = argparse.ArgumentParser(description="Image Downloader")
parser.add_argument('-f', '--file', type=str, help='Generate url and download images based on json config file')
parser.add_argument('-d', '--destination', type=str, default='', help='The folder where images will be downloaded to')
args = parser.parse_args()

async def main(args):
    extractor = Extractor('patterns.json')
    if args.file: source = URLGenerator.source(args.file)
    else: source = ClipboardReader.source
    visited = set()
    if args.destination: folder = args.destination
    else: folder = 'images/'
    if not os.path.isdir(folder): return
    
    count = 1
    async for target in source():
        if not extractor.input.match(target): continue
        content, url = await Downloader.downloadContent(target)
        if url in visited: break
        visited.add(url)
            
        for img in extractor.resource.finditer(content):
            if not img.group(): continue
            link = img.group()
            name = link.split('/')[-1] + '.png'
            await Downloader.downloadFile(link, os.path.join(folder, name))

            print('\033[K\033[A')
            print('Downloading ' + '.' * count, end='\r')
            count = (count + 1) % 5 + 1

    await waitTilFinish()

async def waitTilFinish():
    await asyncio.sleep(0.4)
    while len(asyncio.Task.all_tasks()) > 1:
        await asyncio.sleep(0.4)
    
asyncio.run(main(args))
print('Completed')
