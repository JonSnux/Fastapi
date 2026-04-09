# TODO: Создайте корутину, которая ждет 5 секунд.
#  Запустите ее как задачу и отмените ее через 2 секунды.

import asyncio

async def waiter_coro():
    print("Ready to wait 5 secs")
    await asyncio.sleep(5)


async def main():
    task = asyncio.create_task(waiter_coro())

    seconds_elapsed = 0
    while not task.done():
        print("Checking in a second")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 2:
            task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("The task was cancelled after 2 secs")


asyncio.run(main())