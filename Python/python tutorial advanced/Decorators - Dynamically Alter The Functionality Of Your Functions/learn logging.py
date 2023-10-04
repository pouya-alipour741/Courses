from functools import wraps

def logger(original_func):
    import logging
    logging.basicConfig(filename=f'{original_func.__name__}',level=logging.INFO)

    # @wraps explained in line 41
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(f'ran with args{args} and kwargs{kwargs}')
        return original_func(*args, **kwargs)
    return wrapper


def timer(original_func):
    import time


    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 =time.time() - t1
        print(f'{original_func.__name__} ran in {t2}seconds')
        return result
    return wrapper


# @logger
# def display_info(name,age):
#     print(f'display info ran with {name} and {age}')
#
# display_info('pouya',32)
#
# @timer
# def display_info(name,age):
#     import time
#     time.sleep(1)
#     print(f'display info ran with arguments ({name} ,{age})')
#
# display_info('pouya',32)


# for combining multiple wrappers in this example we need to use the wraps() decorator on each wrapper to return function name instead of wrapper
# @timer
# @logger
# def display_info(name,age):
#     import time
#     time.sleep(1)
#     print(f'display info ran with arguments ({name} ,{age})')
#
# display_info('john',43)
#
# print(logger(display_info).__name__)

