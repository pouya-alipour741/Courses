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


class Developer(Employee):
    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
    raise_amount = 1.10
class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->>', emp.fullname())



# emp_1 = Employee('pouya','alipour',3000)
# emp_2 = Employee('gary','nevil',5000)
# emp_3 = Employee('mary','jane',2000)

# dev_1 = Developer('john','green',9000,'python')
# dev_2 = Developer('gary','mcclane',8000, 'java')
# print(help(dev_1))  #shows method resolution at top of the list and other stuff
# print(dev_1.fullname())

# mg_1 = Manager('Suzy','bebet',20000,[dev_1,dev_2])
# mg_2 = Manager('gareth','bale',50000)
# print(mg_1.email)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# mg_1.add_emp(emp_3)
# mg_1.print_emps()
# mg_2.print_emps()

#isintance and issubclass builtins
# print(isinstance(dev_1,Employee))
# print(issubclass(Manager,Employee))


###more on super()
# class Portishead:
#     def __init__(self):
#         print("Portishead")
#
# class KanyeWest(Portishead):
#     def __init__(self):
#         print("KanyeWest")
#         # Portishead.__init__(self)
#         super().__init__()  ###same as above but more practical

# kanye = KanyeWest()
# print(kanye)


###Diamond inheritance
# class Portishead:
#     def __init__(self):
#         print("Portishead")
#
# class KanyeWest(Portishead):
#     def __init__(self):
#         print("KanyeWest")
#         Portishead.__init__(self)
#
# class ASAPRocky(Portishead):
#     def __init__(self):
#         print("ASAPRocky")
#         Portishead.__init__(self)
#
# class ASAPSebbie(KanyeWest,ASAPRocky):
#     def __init__(self):
#         print("ASAPSebbie")
#         KanyeWest.__init__(self)
#         ASAPSebbie.__init__(self)
#
# sebbie = ASAPSebbie()


###diamond inheritance with super() which fixed the problem of extra duplicate functions
class Portishead:
    def __init__(self):
        print("Portishead")

class KanyeWest(Portishead):
    def __init__(self):
        print("KanyeWest")
        super().__init__()

class ASAPRocky(Portishead):
    def __init__(self):
        print("ASAPRocky")
        super().__init__()

class ASAPSebbie(KanyeWest,ASAPRocky):
    def __init__(self):
        print("ASAPSebbie")
        super().__init__()

sebbie = ASAPSebbie()
