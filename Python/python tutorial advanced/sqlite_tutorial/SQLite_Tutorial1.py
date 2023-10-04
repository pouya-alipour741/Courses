import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()


###string = text  int = integer    float=real     binary= blob
# c.execute("""CREATE TABLE employees (
#                 first text,
#                 last text,
#                 pay integer
#                 )""")
#
# c.execute("INSERT INTO employees VALUES('john','doe',5000)")

conn.commit()

c.execute("SELECT * FROM employees WHERE pay= 5000")

conn.commit()

print(c.fetchmany(2))   #c.fetchmany(5)   c.fetchall()


conn.close()

