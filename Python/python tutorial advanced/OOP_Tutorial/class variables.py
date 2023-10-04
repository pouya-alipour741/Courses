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

        Employee.num_emp += 1 # we create it in init section because everytime we make a new instance init method runs #also we don't need to say self.num_emp here because it's a constant value and there is no need to override it with instances

    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   ##can also use Employee.raise_amount but changing instance variables like emp_1.raise_amount = 1.07 would not have effect here



emp_1 = Employee('pouya','goldberg',3000)
emp_2 = Employee('gary','nevil',5000)
emp_3 = Employee('mary','jane',2000)

##1
# emp_1.first = 'bill'
# print(emp_1.first)
# print(emp_1.email)
# print(emp_2.fullname())
# #this is same as above
# print(Employee.fullname(emp_2))
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(Employee.num_emp)
# print(emp_1.num_emp)

###2
# emp_1.raise_amount = 1.07
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
#
# emp_1.apply_raise()  ##if in line 17 we have self.raise_amount this works but if we have Employee.raise_amount this would not work and we have to say Employee.raise_amount = 1.07
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


