import asyncio, os

async def source():
    visited = set()
    while True:
        text = os.popen('pbpaste', 'r').read()
        if not text or text in visited:
            await asyncio.sleep(1); continue
        visited.add(text)
        yield text
