from operator import attrgetter
import operator

# li = [-5,-3,6,9]
# sorted_li = sorted(li,key=abs)        ###we can use li.sort() method but it does not need to be assigned to a variable and it does not work for non list
# print(sorted_li)

# d1 = {'name':'pouya','job':'programming','habit':'zz','os':'windows'}
# sorted_dic1 = sorted(d1)        ##by default it sorts by keys
# sorted_dic2 = sorted(d1.items())
# sorted_dic3 = sorted(d1.values())
# print('default sort=',sorted_dic1)
# print('sort by items=',sorted_dic2)
# print('sort by values=',sorted_dic3)


##practice
# dict = {}
# for i in sorted_dic2:
#     dict[i[0]] = i[1]
# print(dict)

# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def __repr__(self):
#         return f'({self.name},{self.age}, ${self.salary})'
#
# e1 = Employee('john',33,78000)
# e2 = Employee('frank',40,100000)
# e3 = Employee('mary',34,65000)
# employees = [e1, e2, e3]
# def sorted_employees(emp):
#     return emp.age
#
# #
# s_employees = sorted(employees,key=sorted_employees,reverse=True)  #key=lambda emp:emp.name # key=attrgetter('age') #key=sorted_employees
#
# print(s_employees)


# list of dictionaries
# people = [
#     {
#         'name': 'John Doe',
#         'city': 'Gotham',
#         'state': 'NY'
#     },
#     {
#         'name': 'Jane Doe',
#         'city': 'Kings Landing',
#         'state': 'NY'
#     },
#     {
#         'name': 'Corey Schafer',
#         'city': 'Boulder',
#         'state': 'CO'
#     },
#     {
#         'name': 'Al Einstein',
#         'city': 'Denver',
#         'state': 'CO'
#     },
#     {
#         'name': 'John Henry',
#         'city': 'Hinton',
#         'state': 'WV'
#     },
#     {
#         'name': 'Randy Moss',
#         'city': 'Rand',
#         'state': 'WV'
#     },
#     {
#         'name': 'Nicole K',
#         'city': 'Asheville',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jim Doe',
#         'city': 'Charlotte',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jane Taylor',
#         'city': 'Faketown',
#         'state': 'NC'
#     }
# ]


# sorted_ppl = sorted(people,key=lambda  i:i['city'])

# sorted_ppl = sorted(people,key=operator.itemgetter('name'))
# print(sorted_ppl)

# for i in sorted_ppl:
#     print(i)

