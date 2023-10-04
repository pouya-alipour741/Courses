class Employee:
    num_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@gmail.com'
        Employee.num_emp += 1 # we create it in init section because everytime we make a new instance init method runs
    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod  #changes class variable instead of  instance variable so it affect all instances at once
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod                           #first,last,pay = emp.split('-')  emp_1 = Employee(first,last,pay)   turned into function
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod  #sometimes you need a function that does need any of instance nor class variables but still somewhat relatable to your class
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#ex 1
emp_1 = Employee('pouya','goldberg',3000)
emp_2 = Employee('gary','nevil',5000)
emp_3 = Employee('mary','jane',2000)

emp_1.set_raise_amount(1.08)
print(Employee.raise_amount)
print(emp_3.raise_amount)
print(emp_1.raise_amount)
#ex 2 #using classmethod as alternative constructor
# emp_str_1 = 'john-doe-7000'
# emp_str_2 = 'bill-golden-2000'
# emp_str_3 = 'mark-walden-12000'

# emp_1 = Employee.from_string(emp_str_1)
# print(emp_1.fullname())
# emp_2 = Employee.from_string(emp_str_2)
# emp_3 = Employee.from_string(emp_str_3)
# print(emp_2.fullname())
# print(emp_3.fullname())
#ex3 static methods
import datetime
my_date = datetime.date(2022,7,11)
print(Employee.is_work_day(my_date))







