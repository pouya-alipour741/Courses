#salam va hello ra ba ham yeki be darmian edgham konid
##def gen1():
##    for i in 'salam':
##        yield i
##def gen2():
##    for j in 'hello':
##        yield j
##
##a = gen1()   
##b = gen2()
##
##
##my_str = ''
##for i in range(len('salam')):
##    my_str = my_str + next(a) + next(b)
##print(my_str)



#dars
##def func(a,b,*c):
##    return a+b+sum(c)
##
##a = func(2,4,7,1,3,4,7)



##def func(a,b,*args,**kwargs):  
##    return a + b + sum(args) + sum(kwargs.values())
##
##a = func(10,20,3,2,c = 100, d = 30)



##from math import log,sin,cos
##print(log(100))
##
##from math import *
##print(log(100))
##
##import math as m
##print(m.log(100))

##print(chr(97))
##print(ord('a'))
##print(ord('z'))


##for i in range(200):
##    print(i,chr(i))


##a = '434'
##print(a.isnumeric())
##print(a.isdigit())
##print(a.isalpha()) #faghat horuf
##print(a.isalnum()) #horuf ya addad


##st1 = [1,2,3,4,5,6]
##import random
##a = random.choice(st1)
##b = random.randint(45,55)
##c = random.random()  #0<c<1
##random.shuffle(st1)


##a = bin(20)
##b = hex(20)
##c = int('14',16)  #hex 14 ro tabdil kon be adad


##import math
##a = math.pi
##b = math.inf
##c = math.e


##def func(a):
##    return a**2

##lst = [1,2,3,4,5,6]

##lst2 = []
##for i in lst:
##    lst2.append(func(i))
##z = map(func,lst)  #javab shabih bala  #baraye functionaye gheyr az boolean


##lst = [1,2,3,4,5,6]
##def func(a):
##    return a<4
##z = filter(func,lst)  #baraye functionayi boolean true false


##func = lambda *args,a=2,c=3, : a * c /sum(args)
##a = func(2,3,5)

##lst = [1,2,3,4]
##z = map(lambda a:a**2 , lst)

##import random
##def gen():   
##    for i in range(1000000):
##        yield random.random() * i ** 2
##



