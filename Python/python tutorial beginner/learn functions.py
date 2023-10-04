# def hello_func(greeting,name='You'):
#     return f'{greeting} {name}'
#
# print(hello_func('hi'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['math','geology']
info = {'name':'pouya','age':32}
student_info(*courses,**info)