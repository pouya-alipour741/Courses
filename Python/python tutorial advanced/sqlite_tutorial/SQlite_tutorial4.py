import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('CREATE TABLE employees(first text,last text,pay integer)')


# def insert_emp(emp):
#     with conn:
#         c.execute('INSERT INTO employees VALUES(:first,:last,:pay)',{'first':emp.first,'last':emp.last,'pay':emp.pay})

###or write it with ? placeholder
def insert_emp(emp):
    with conn:
        c.execute('INSERT INTO employees VALUES(?,?,?)',(emp.first,emp.last,emp.pay))


def get_emp_by_name(firstname):
    c.execute('SELECT * FROM employees WHERE first=:first',{'first':firstname})
    return c.fetchall()


def remove_emp(emp):
    with conn:
        c.execute('DELETE FROM employees WHERE first= :first and last= :last',{'first':emp.first,'last':emp.last})


def update_pay(emp,pay):
    with conn:
        c.execute('''UPDATE employees SET pay=:pay 
                    WHERE first=:first and last=:last''',
                  {'first': emp.first,'last': emp.last,'pay': pay})


emp1 = Employee('corey','schafer',8000)
emp2 = Employee('jim','schafer',8000)

insert_emp(emp2)
print(get_emp_by_name(emp2.first))

update_pay(emp2,18000)
print(get_emp_by_name(emp2.first))

remove_emp(emp2)
print(get_emp_by_name(emp2.first))
