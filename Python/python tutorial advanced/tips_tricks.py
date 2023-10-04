# person_info = {'first':'pouya','last':'alipour'}
#
# class Person():
#     pass
#
# person = Person()
#
# setattr(person,'pay', 4000)
# pay = getattr(person,'pay')
# # print(pay)
#
#
# ##can also use it in variable in loop
# for key,value in person_info.items():
#     setattr(person,key,value)
#
# for key in person_info.keys():
#     print(getattr(person,key))

########hide password with input
# from getpass import getpass
#
# user = input('username: ')
# passw = getpass('password: ')     ###run in terminal to hide password
#
# if passw == 'admin':
#     print('logged in...')
# else:
#     print('not authorized')


###inserting mutables in arguements problems
# def add_employee(emp,emp_list = []):
#     emp_list.append(emp)
#     print(emp_list)
#
# print(add_employee.__defaults__)
# add_employee('john')
# print(add_employee.__defaults__)
# add_employee('pouya')
# print(add_employee.__defaults__)

# def add_employee_fixed(emp,emp_list =None):
#     if emp_list is None:
#         emp_list = []
#     emp_list.append(emp)
#     print(emp_list)
#
# print('\nfixed version')
# print(add_employee_fixed.__defaults__)
# add_employee_fixed('john')
# print(add_employee_fixed.__defaults__)
# add_employee_fixed('pouya')
# print(add_employee_fixed.__defaults__)

###2nd exmaple
# import time
# from datetime import datetime
#
# def display_time(time_to_print=datetime.now()):
#     print(time_to_print.strftime("%B %d, %Y %H:%M:%S"))
#
# print(display_time.__defaults__)
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)
# display_time()
#
# ###fixed
#
# def display_time_fixed(time_to_print=None):
#     if time_to_print is None:
#        time_to_print = datetime.now()
#     print(time_to_print.strftime("%B %d, %Y %H:%M:%S"))
#
# print(display_time_fixed.__defaults__)
# display_time_fixed()
# time.sleep(1)
# display_time_fixed()
# time.sleep(1)
# display_time_fixed()

#####quick tip : generators can only be looped and accessed once then they become exhausted


##divmod() gives back a tupple like this (divisor,remainder)
# s = 7659
# minutes,seconds = divmod(s,60)
# hours,minutes = divmod(minutes,60)
# print(f'{s} seconds equals to {hours} hours and {minutes} minutes and {seconds} seconds')
# print(f'{hours}:{minutes:02}:{seconds}')


####map function extra
# a = [1,2,3,4]
# b = [5,6,7,8]
#
# print(list(map(lambda x,y,z:x+y-2*z,a,b,a)))  ###foz z value ,uses a again