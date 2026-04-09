import asyncio

async def my_coro(n: int):
    await asyncio.sleep(10)
    print(f"Coro {n} complete")
    return(f"Result {n}")


async def main():
    long_task = asyncio.create_task(my_coro(1))
    seconds_elapsed = 0

    while not long_task.done():
        print("Task not finished, checking in a second")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except asyncio.CancelledError:
        print("The task was cancelled")

if __name__ == "__main__":
    asyncio.run(main())