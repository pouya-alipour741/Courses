def timer(original_func):
    def wrapper(*args,**kwargs):
        import time
        t1 = time.time()
        result = original_func(*args,**kwargs)
        t2 = time.time() - t1
        print(f'{original_func.__name__} ran in {t2} seconds')
        return result
    return wrapper


@timer
def display_info(name,age):
    import time
    time.sleep(1)
    print(f'display info ran with arguements {name} and {age}')
display_info('Pouya',32)

