from concurrent.futures import ThreadPoolExecutor
import time
import requests

def download(url):
    print(f"Starting download: {url}")
    resp = requests.get(url)
    print(f"Finished: {url} | Size: {len(resp.content)}")

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.wikipedia.org"
]

start = time.time()

# Create a pool with 3 threads
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(download, urls)

print(f"Total time: {time.time() - start:.2f} sec")
