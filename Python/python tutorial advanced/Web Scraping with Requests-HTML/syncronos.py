from requests_html import HTMLSession
import time

t1 = time.perf_counter()

session = HTMLSession()

r = session.get(' https://httpbin.org/delay/1')
response = r.html.url
print(response)

r = session.get(' https://httpbin.org/delay/2')
print(r.html.url)

r = session.get(' https://httpbin.org/delay/3')
print(r.html.url)

t2 = time.perf_counter()

print(f'sync time is {t2 - t1}')
