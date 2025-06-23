import aiohttp
import asyncio
import logging
import time

start = time.time()

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

urls = ['https://example.com', 'https://www.youtube.com', 'https://jsonplaceholder.typicode.com']

async def fetch(session, url):
    logging.info(f"Awaiting response {url}")
    async with session.get(url) as response:
        status = response.status
        logging.info(f"Response for {url} acquired with status code {status}")
        await response.text()
        return status

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())

print(f'time: {time.time() - start}')