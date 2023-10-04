def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper(*args, **kwargs):
            print(f'{prefix}executed before {original_function.__name__}')
            result = original_function(*args, **kwargs)
            print(f'{prefix}executed after {original_function.__name__}\n')
            return result
        return wrapper
    return decorator_function

@prefix_decorator('logger:')
def display_info(name, age):
    print(f"ran with arguments ({name},{age})")

display_info('pouya',32)
display_info('john',35)

