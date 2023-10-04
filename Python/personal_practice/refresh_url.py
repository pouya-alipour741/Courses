import webbrowser
from time import sleep
from itertools import count

url = input('Input the URL to reload, including "http://: ')

counter = count(start=1)
while True:
    print(f"refreshing...try number {next(counter)}")
    webbrowser.open(url, new=0)
    sleep(180)