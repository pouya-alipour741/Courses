import time

##timer decorator

def timer_args(prefix):

    def timer(orig_func):
        import time

        def wrapper(*args, **kwargs):
            t1 = time.perf_counter()
            print(prefix, f"ran before {orig_func.__name__}")
            orig_func(*args, **kwargs)
            print(prefix, f"ran after {orig_func.__name__}")
            t2 = time.perf_counter()
            t3 = t2-t1
            time_it = print(f"{orig_func.__name__} ran in {t3} seconds")
            return time_it
        return wrapper
    return timer


##logging decorator
def logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}",level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"ran with args{args} and kwargs{kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


@timer_args("testing:")
def display_info(name,age):
    time.sleep(1)
    print(f"name: {name}, age:{age}")

display_info("pouya", 33)
