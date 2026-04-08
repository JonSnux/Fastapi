import asyncio
import aiohttp

async def fetch_data(session, url):
    response = await session.get(url)
    try:
        return await response.json()
    finally:
        response.close()


async def main():
    async with aiohttp.ClientSession() as session:
        coros = [fetch_data(session, "https://api.kanye.rest") for _ in range(5)]

        results = []
        for coro in coros:
            task_instance = asyncio.create_task(coro)
            results.append(task_instance)

        for result in asyncio.as_completed(results):
            print(await result)


if __name__ == "__main__":
    asyncio.run(main())
        