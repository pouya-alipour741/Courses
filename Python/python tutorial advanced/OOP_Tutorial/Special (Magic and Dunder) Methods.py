import random
random_domains = ['gmail.com','yahoo.com','mail.ir']

class Employee:
    num_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@{random.choice(random_domains)}'
        Employee.num_emp += 1 # we create it in init section because everytime we make a new instance init method runs
    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    def __repr__(self): #this special method is mostly for debugging and coders
        return f'Employee("{self.first}", "{self.last}", {self.pay})'
    def __str__(self): #this special method is mostly for plain eyes and reading
        return f'{self.fullname()} with {self.pay} salary per year'
    def __add__(self, other):
            return self.pay + other.pay
    def __sub__(self, other):
        return self.pay - other.pay
    def __len__(self): #customize len  with this special method
        return len(self.fullname())


emp_1 = Employee('pouya','goldberg',3000)
emp_2 = Employee('gary','nevil',5000)
emp_3 = Employee('mary','jane',2000)

print(repr(emp_2))  #same as print(emp_1.__repr__())  or same for "pouya".__len__() vs len('pouya')
print(str(emp_2))
print(emp_3)

print()
print(emp_1 + emp_3)  # we want to turn this into working functions so we define __add__ and etc
print(emp_2 - emp_1)
print(len(emp_1))








