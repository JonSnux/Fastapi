# TODO: Создайте несколько асинхронных задач с разными задержками.
#  Используйте asyncio.as_completed() для обработки результатов задач по мере их завершения.
#  Выведите результаты каждой задачи сразу после ее завершения.
import random
import asyncio

async def delayed_coro():
    delay = random.randint(0, 5)
    print(f"Will sleep for {delay} secs")
    await asyncio.sleep(delay)
    print(f"finished in {delay} secs")

async def main():
    tasks = [asyncio.create_task(delayed_coro()) for _ in range(5)]

    for task in tasks:
        if asyncio.as_completed(task):
            await task

print(asyncio.run(main()))
