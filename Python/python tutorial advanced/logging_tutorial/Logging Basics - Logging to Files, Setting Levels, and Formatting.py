import logging
import random
import os

path = os.path.dirname(os.path.abspath(__file__))
logfile = f"{path}\\app1.log"

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s',filename=logfile)   ##you can use filemode= 'w'  ,default is 'a'

# print(__file__)  ##file address
# 1
# def add(x,y):
#     return x + y
#
# def sub(x,y):
#     return x - y
#
# def divide(x,y):
#     return x/y
#
# num1 = 20
# num2 = 10
#
# def mult(x,y):
#     return x * y
#
# add_res = add(num1,num2)
# logging.debug(f'add: {num1}+{num2}={add_res}')
#
# sub_res = sub(num1,num2)
# logging.debug(f'sub: {num1}-{num2}={sub_res}')
#
# divide_res = divide(num1,num2)
# logging.debug(f'divide: {num1}/{num2}={divide_res}')
#
# mult_res = mult(num1,num2)
# logging.debug(f'mult: {num1}*{num2}={mult_res}')



# # 2 import kardim bedune niaz be code paeen kar mikone
# logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(levelname)s:%(message)s')
#
# class Employee:
#     num_emp = 0
#     raise_amount = 1.05
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         Employee.num_emp += 1 # we create it in init section because everytime we make a new instance init method runs
#         logging.debug(f'{self.fullname} & {self.email} has been created')
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@gmail.com'
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# emp_1 = Employee('pouya','goldberg',3000)
# emp_2 = Employee('gary','nevil',5000)
# emp_3 = Employee('mary','jane',2000)



