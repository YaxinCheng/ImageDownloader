import asyncio, requests
from concurrent.futures import ThreadPoolExecutor

async def downloadContent(url, dst: str=None) -> (str, str):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        response = await loop.run_in_executor(pool, requests.get, url)
    if dst:
        async with open(dst, 'w') as storeFile:
            storeFile.write(response.content)
    return response.text, response.url

async def downloadFile(url, dst: str):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        response = await loop.run_in_executor(pool, requests.get, url)
    with open(dst, 'wb') as storeFile:
        storeFile.write(response.content)