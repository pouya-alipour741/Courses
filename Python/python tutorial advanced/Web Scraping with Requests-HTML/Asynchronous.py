from requests_html import AsyncHTMLSession
import time

assesion = AsyncHTMLSession()

async def get_delay1():
   r = await assesion.get(' https://httpbin.org/delay/1')
   return r


async def get_delay2():
    r = await assesion.get('https://httpbin.org/delay/2')
    return r


async def get_delay3():
    r = await assesion.get('https://httpbin.org/delay/3')
    return r

t1 = time.perf_counter()

results = assesion.run(get_delay1,get_delay2,get_delay3)

for result in results:
    response = result.html.url
    print(response)

t2 = time.perf_counter()

print(f'Async time is {t2 - t1}')

