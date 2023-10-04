def logger(original_func):
    import logging
    logging.basicConfig(filename= f'{original_func.__name__}', level= logging.INFO)
    def wrapper(*args,**kwargs):        
        logging.info(f'ran with args{args} and kwargs{kwargs}')
        return original_func(*args,**kwargs)
    return wrapper

@logger
def display_info(name,age):
    print(f'display_info ran with {name} and {age}')

display_info('Pouya',32)
