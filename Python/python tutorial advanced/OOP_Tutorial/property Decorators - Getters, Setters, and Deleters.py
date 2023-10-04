import random
random_domains = ['gmail.com','yahoo.com','mail.ir']

class Employee:
    num_emp = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f'{self.first}.{self.last}@{random.choice(random_domains)}'
        Employee.num_emp += 1 # we create it in init section because everytime we make a new instance init method runs

    @property
    def email(self):
        return f'{self.first}.{self.last}@{random.choice(random_domains)}'
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    @fullname.setter
    def fullname(self,name):
        self.first, self.last = name.split(' ')
    @fullname.deleter
    def fullname(self):
        print('deleter worked')
        self.first = None
        self.last = None


emp_1 = Employee('pouya','goldberg')
emp_2 = Employee('gary','nevil')
emp_3 = Employee('mary','jane')

emp_1.first = 'bill'  #as we can see our email name has not changed because self.email
                     #as atribute is not using updated instances so we can use property decorator on newly created email function without the need to break our codes

emp_1.fullname = 'gareth bale'  #we get error for doing this so we use setter decorator and make new function with it
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname #with the help of deleter decorator
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

