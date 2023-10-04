import logging

logging.basicConfig(filename='employee.log',level=logging.DEBUG,format='%(levelname)s:%(message)s')


class Employee:
    num_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_emp += 1 # we create it in init section because everytime we make a new instance init method runs
        logging.debug(f'{self.fullname} & {self.email} has been created')
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('pouya','goldberg',3000)
emp_2 = Employee('gary','nevil',5000)
emp_3 = Employee('mary','jane',2000)

