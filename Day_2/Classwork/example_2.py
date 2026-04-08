import asyncio
import random 

async def my_coro(n: int):
    print(f"Coro {n} start")
    delay = random.uniform(1,4)
    await asyncio.sleep(delay)
    print(f"Coro {n} complete")
    return(f"Result {n} in {delay} secs")


async def main():
    task1 = asyncio.create_task(my_coro(1))
    task2 = asyncio.create_task(my_coro(2))
    task3 = asyncio.create_task(my_coro(3))

    results = await asyncio.gather(task1, task2, task3)

    print(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())