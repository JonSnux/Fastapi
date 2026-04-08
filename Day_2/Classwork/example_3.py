import asyncio
import random 

async def my_coro(n: int):
    print(f"Coro {n} start")
    delay = random.uniform(1,4)
    await asyncio.sleep(delay)
    print(f"Coro {n} complete")
    return(f"Result {n} in {delay} secs")


async def main():
    tasks = [asyncio.create_task(my_coro(i)) for i in range(1,4)]

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f"Got result: {result}")


if __name__ == "__main__":
    asyncio.run(main())