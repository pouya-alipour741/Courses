import time
import multiprocessing


###1
# start = time.perf_counter()
# def do_something(seconds):
#     print(f'sleeping in {seconds} second(s)')
#     time.sleep(seconds)
#     print('done sleeping...')
#
# if __name__ == "__main__":     ###must be done on windows for multiprocessing else  script won't work
#
#     p1 = multiprocessing.Process(target=do_something,args=(1.5,))
#     p2 = multiprocessing.Process(target=do_something,args=(1.5,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     finish = time.perf_counter()
#     print(f'finished in {finish-start} seconds')



###2
# start = time.perf_counter()
# def do_something(seconds):
#     print(f'sleeping in {seconds} second(s)')
#     time.sleep(seconds)
#     print('done sleeping...')
#
# if __name__ == "__main__":
#     processes = []
#     secs= [5,4,3,2,1]
#     for sec in secs:
#         p = multiprocessing.Process(target=do_something,args=(sec,))
#         p.start()
#         processes.append(p)
#
#     for process in processes:
#         process.join()
#
#     finish = time.perf_counter()
#     print(f'finished in {finish-start} seconds')