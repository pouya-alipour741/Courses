import sqlite3

conn = sqlite3.connect('employees_draft.db')

c = conn.cursor()


###string = text  int = integer    float=real     binary= blob
# c.execute("""CREATE TABLE employees (
#                 first text,
#                 last text,
#                 pay integer
#                 )""")
#
# personel_lst = [('john','doe',5000),('pouya','alipour',9000)]
# c.executemany("INSERT INTO employees VALUES(?,?,?)",personel_lst)

# conn.commit()
#
# c.execute("SELECT * FROM employees WHERE pay= 5000")
#
# conn.commit()
#
# print(c.fetchall())   #c.fetchmany(5)   c.fetchall()

# for row in c.execute("select * from employees where first=?",('pouya',)):
c.execute("select * from employees")
employee_search = c.fetchall()
print(employee_search)


conn.close()

