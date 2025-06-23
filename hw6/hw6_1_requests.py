import logging
import requests
import time

start = time.time()

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

urls = ['https://example.com', 'https://www.youtube.com', 'https://jsonplaceholder.typicode.com']

for url in urls:
    logging.info(f"Awaiting response {url}")
    response = requests.get(url)
    logging.info(f"Response for {url} acquired with status code {response.status_code}")

print(f'time: {time.time() - start}')