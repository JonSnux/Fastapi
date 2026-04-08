import httpx
import time
import asyncio

urls = ("https://example.com", "https://vk.com")

def sync_call() -> None:
    for url_no in range(len(urls)):
        response = httpx.get(urls[url_no], verify=False)
        print("Status code:", response.status_code)



async def async_call(url):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        print(r.status_code)


async def async_call_all(local_urls):
    return await asyncio.gather(*[async_call(url) for url in local_urls])

print("running sync")
sync_start = time.perf_counter()
sync_call()
sync_call()
sync_end = time.perf_counter()

print(f"Выполнение кода заняло: {sync_end - sync_start:.4f} c.")

print("running async")
async_start = time.perf_counter()
asyncio.run(async_call_all(urls))
async_end = time.perf_counter()

print(f"Выполнение кода заняло: {async_end - sync_start:.4f} c.")