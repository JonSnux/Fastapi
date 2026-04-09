import asyncio

async def my_coro(n: int):
    await asyncio.sleep(10)
    print(f"Coro {n} complete")
    return(f"Result {n}")


async def main():
    task = asyncio.create_task(my_coro(1))


    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.TimeoutError:
        print(f"Check: {task.cancelled()}")
        result = await task
        print(f"{result = }")

if __name__ == "__main__":
    asyncio.run(main())