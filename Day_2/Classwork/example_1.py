import asyncio

async def my_coro(n: int):
    print(f"Coro {n} start")
    await asyncio.sleep(1)
    print(f"Coro {n} complete")
    return(f"Result {n}")


async def main():
    task1 = asyncio.create_task(my_coro(1))
    task2 = asyncio.create_task(my_coro(2))

    result1 = await task1
    result2 = await task2

    print(f"Results: {result1}, {result2}")

if __name__ == "__main__":
    asyncio.run(main())