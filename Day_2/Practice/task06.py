# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.

import asyncio
import aiohttp
import time

#Можно ли здесь каким-либо образом использовать менеджер контекста, чтобы не открывать и не закрывать сессию явно?
async def request(session, url):  
    response = await session.get(url)
    try:
        return await response.text() #не получилось с json(), ошибки mimetype
    finally:
        await session.close()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        coros = [request(session, url) for url in urls]

        tasks =[]
        for coro in coros:
            task = asyncio.create_task(coro)
            tasks.append(task)
        for result in asyncio.as_completed(tasks):
            return len(await result)

urls = [
    "https://yandex.ru",
    "https://google.com",
    "https://python.org"
]

start_time = time.perf_counter()
result = asyncio.run(main(urls))
end_time = time.perf_counter()

print(f"Received {result} bytes")
print(f"Completion time: {end_time - start_time:.2f}")