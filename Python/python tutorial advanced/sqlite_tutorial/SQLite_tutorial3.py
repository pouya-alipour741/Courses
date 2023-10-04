import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')    ##using :memory: start a table from scratch everytime we run this,it's good when we want to test new stuff to avoid duplicates and errors

c = conn.cursor()

c.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")

emp1 = Employee('corey','schafer',8000)
emp2 = Employee('jim','schafer',8000)

c.execute("INSERT INTO employees VALUES(?,?,?)",(emp1.first,emp1.last,emp1.pay))    ####using placeholder ?

conn.commit()


c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp2.first,'last':emp2.last,'pay':emp2.pay})         #using placeholder of dictionary like

conn.commit()

#
c.execute("SELECT * FROM employees WHERE pay=?" ,(5000,))

conn.commit()

print(c.fetchall())

c.execute("SELECT * FROM employees WHERE pay= :pay" ,{'pay':8000})

conn.commit()

print(c.fetchmany(2))   #c.fetchmany(5)   c.fetchall()


conn.close()