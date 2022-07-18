import sqlite3
from employee import employee_demo
con = sqlite3.connect('employee.db')

c= con.cursor()

# c.execute("""CREATE TABLE employees(
#             first text,
#             last text,
#             pay integer
#             )""") 
#adds a table name employees with columns for first(text), last(text) and pay(integer)

#c.execute ("INSERT INTO employees VALUES('Mary','Schafer','50000')") 
#adds values to employee.db
# con.commit()

emp_1 = employee_demo('John',"Doe",80000)
emp_2 = employee_demo('Jane',"Doe",90000)

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_1.first,'last':emp_1.last, 'pay':emp_1.pay})

# con.commit() 
# #inserts emp_1 data into employees.db using the columns first, last and pay and mapping it to emp_1 objects

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

# con.commit()

c.execute("SELECT * FROM employees WHERE last=?",('Schafer',)) #other way to query
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'}) # best way to query
print(c.fetchall())

con.commit()
con.close()