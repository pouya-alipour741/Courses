import time
import threading


####1
# start = time.perf_counter()
# def do_something():
#     print('Sleeping 1 second')
#     time.sleep(1)
#     print('done sleeping')
#
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
#
# finish = time.perf_counter()
# print(f'took {round((finish-start),2)} seconds')


####2
# start = time.perf_counter()
#
# def do_something():
#     print('Sleeping 1 second')
#     time.sleep(1)
#     print('done sleeping')
#
# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
# print(f'took {round((finish-start),2)} seconds')


###3
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('done sleeping')

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'took {round((finish-start),2)} seconds')

