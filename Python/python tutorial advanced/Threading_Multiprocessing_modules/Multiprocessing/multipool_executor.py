import time
import concurrent.futures


###1
# start = time.perf_counter()
# def do_something(seconds):
#     print(f'sleeping in {seconds} second(s)')
#     time.sleep(seconds)
#     print(f'done sleeping in {seconds}...')
#
# if __name__ == "__main__":
#
#     secs = [5,4,3,2,1]
#
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = [executor.submit(do_something,sec) for sec in secs]
#
#         for f in concurrent.futures.as_completed(results):
#             print(f.result())
#
#     finish = time.perf_counter()
#     print(f'finished in {finish-start} seconds')


###2
# start = time.perf_counter()
# def do_something(seconds):
#     print(f'sleeping in {seconds} second(s)')
#     time.sleep(seconds)
#     print(f'done sleeping in {seconds}...')
#
# if __name__ == "__main__":
#
#     secs = [5,4,3,2,1]
#
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = executor.map(do_something,secs)
#
#         for result in results:
#             print(result)
#
#     finish = time.perf_counter()
#     print(f'finished in {finish-start} seconds')