# #closure example
# def decorator_function(original_func):
#     def wrap_func():
#         return original_func()
#     return wrap_func
#
# def display():
#     print('display function worked')
#
# display = decorator_function(display)
# display()


def decorator_function(original_func):
    print('ran decorator before wrapper')
    def wrap_func(*args, **kwargs):
        print('wrapper function ran before original_func')
        return original_func(*args, **kwargs)
    return wrap_func


@decorator_function     #same as saying display_info = decorator_function(display_info)
def display_info(name,age):
    print(f'display info ran with arguments {name} and {age}')


display_info('john',25)


# using class for decorators instead of functions ,keep in mind usually people use function method !
# class decorator_class(object):
#     def __init__(self,original_func):
#         self.original_func = original_func
#     def __call__(self, *args, **kwargs):
#         print(f'call method ran before {self.original_func.__name__}')
#         return self.original_func(*args, **kwargs)
#
# @decorator_class
# def display_info(name,age):
#     print(f'display info ran with arguments {name} and {age}')
#
# display_info('john',25)





