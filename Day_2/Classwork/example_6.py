import asyncio

async def my_coro(n: int):
    await asyncio.sleep(2)
    print(f"Coro {n} complete")
    return(f"Result {n}")


async def main():
    task = asyncio.create_task(my_coro(1))
    task.cancel()
    print(f"The task is cancelled: {task.cancelled()}")
    try:
        await task
    except asyncio.CancelledError:
        print("The task was cancelled")

if __name__ == "__main__":
    asyncio.run(main())