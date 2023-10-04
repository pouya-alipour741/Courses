import time
import concurrent.futures


###!
# start = time.perf_counter()
#
#
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)')
#     time.sleep(seconds)
#     return 'done sleeping'
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something,1)
#     f2 = executor.submit(do_something,1)
#     print(f1.result())
#     print(f2.result())

# finish = time.perf_counter()
#
# print(f'took {round((finish-start),2)} seconds')


####2
# start = time.perf_counter()
#
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)')
#     time.sleep(seconds)
#     return 'done sleeping'
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_something,1) for _ in range(10)]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#
# finish = time.perf_counter()
#
# print(f'took {round((finish-start),2)} seconds')

####3 it prints out by order that which ended first
# start = time.perf_counter()
#
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)')
#     time.sleep(seconds)
#     return f'done sleeping in {seconds} second(s)'
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5,4,3,2,1]
#     results = [executor.submit(do_something,sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#
# finish = time.perf_counter()
#
# print(f'took {round((finish-start),2)} seconds')

###4  it prints out by order that which started first
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'done sleeping in {seconds} second(s)'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something,secs)

    for result in results:        ###if you need to handle exceptions this part is the place for it
        print(result)

finish = time.perf_counter()

print(f'took {round((finish-start),2)} seconds')

