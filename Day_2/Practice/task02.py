# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их параллельно и соберите результаты в список.

import asyncio

results_list = ["some", "word", "for coro", "to return"]

async def my_coro(string):
    await asyncio.sleep(1)
    print("Coro finished")
    
    return string

async def main(strings):
    tasks = [my_coro(string) for string in strings]

    results = await asyncio.gather(*tasks)
    return results

print(asyncio.run(main(results_list)))