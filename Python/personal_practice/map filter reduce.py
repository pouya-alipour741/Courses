###filter
# lst = [1,2,3,4,5,6]
# def func(a):
#    return a<4
# z = filter(func,lst)  #baraye functionayi boolean true false
#
#
# func = lambda *args,a=2,c=3, : a * c /sum(args)
# a = func(2,3,5)
# print(a)

###map  use a function on each item in the iterable
# lst = [1,2,3,4]
# z = map(lambda a:a**2 , lst)
#
# import random
# def gen():
#    for i in range(1000000):
#        yield random.random() * i ** 2

##2
# a = [1,2,3,4]
# b = [5,6,7,8]
#
# print(list(map(lambda x,y,z:x+y-2*z,a,b,a)))

####Reduce  ##use a function on first 2 elements of iterable until the list is reduce to only one result
from functools import reduce

# ex1
# inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]
#
# lst_len= len(inp_lst)
#
# lst_avg = reduce(lambda x, y: x + y, inp_lst) /lst_len
# print("Average value of the list:\n")
# print(lst_avg)
# print("Average value of the list with precision upto 3 decimal value:\n")
# print(round(lst_avg,3))

##ex2
# factorial = [5,4,3,2,1]
# print(reduce(lambda x,y: x*y,factorial))

##with a simple loop
# start = 1
# for i in factorial:
#     start *= i
# print(start)