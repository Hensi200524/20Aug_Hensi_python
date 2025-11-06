import sqlite3

try:
    db = sqlite3.connect("demodb.db")
    print("Database connected sucsessfully...")
except Exception as e:
    print(e)

#table created 
tbl_create = "CREATE TABLE employee (emp_id integer primary key autoincrement,name varchar(20),department text,salary int(100))"

try:
    db.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)

cr = db.cursor()
#insert data 
"""insert_data = "Insert into employee(name,department,salary)values('neha','management',30000),('Brijesh','It',50000),('Aarti','accountant',4000)"

try:
    db.execute(insert_data)
    db.commit()
    print("record inserted!")
except Exception as e:
    print(e)"""

#update data
"""updt_data = "UPDATE employee set name = 'Dhiren',department = 'Acoount' where emp_id = 3"

try:
    db.execute(updt_data)
    db.commit()
    print("record updated!")
except Exception as e:
    print(e)"""

#delete data
dlt_data = "DELETE from employee where emp_id = 3"

try:
    db.execute(dlt_data)
    db.commit()
    print("record deleted!")
except Exception as e:
    print(e)

#fetch data
show_data = "Select * from employee"

try:
    cr.execute(show_data)
    data = cr.fetchall() #return list
    print(data)

    for i in data:
        print(i)
        
except Exception as e:
    print(e)




