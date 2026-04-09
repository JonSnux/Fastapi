# TODO: Напишите асинхронную программу, которая запускает n асинхронных функции. 
#  n - задайте самостоятельно.
#  Каждая функция должна возвращать случайное целое число в диапазоне от 0 до 10
#  и выполняться за случайное время от 1 до 5 секунд
#  После завершения всех функций найдите сумму всех полученных результатов и выведите её на экран.

from random import randint
import asyncio


async def delayed_returner():
    delay = randint(1, 5)
    print(f"Will sleep for {delay} secs")
    await asyncio.sleep(delay)
    number = randint(1, 10)
    print(f"Will return {number}")
    return number

async def main():
    tasks = [delayed_returner() for _ in range(5)] #Задал n = 5

    results = await asyncio.gather(*tasks)
    sum = 0

    for result in results:
        sum += result
    return sum

answer = asyncio.run(main())
print(f"The sum is: {answer}")