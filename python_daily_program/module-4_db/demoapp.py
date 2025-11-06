import sqlite3

try:
    db = sqlite3.connect('mydb.db')
    print("Database connected...")
except Exception as e:
    print(e)

#table created 
tbl_create = "create table studinfo(id integer primary key autoincrement,name varchar(20),city varchar(20))"

try:
    db.execute(tbl_create)
    print("Table create successfully")
except Exception as e:
    print(e)

#insert data
"""insert_data = "insert into studinfo(name,city)values('Hensi','Morbi'),('Dimpal','Surat'),('Jiya','Vadodra'),('Vicky','morbi'),('Chandres','Wakaner')"

try:
    db.execute(insert_data)
    db.commit()#save data
    print("Insert record successfully..")
except Exception as e:
    print(e)"""

#update data
"""update_data = "update studinfo set name = 'mihit',city = 'jepur' where id = 4"

try:
    db.execute(update_data)
    db.commit()#save data
    print("Update record successfully..")
except Exception as e:
    print(e)"""

#delete data
"""delete_data = "delete from studinfo where id = 2"

try:
    db.execute(delete_data)
    db.commit()#save data
    print("delete record successfully..")
except Exception as e:
    print(e)"""

#show data
cr = db.cursor()
show_data = "select * from studinfo"

try:
    cr.execute(show_data)
    #data= cr.fetchall()
    data = cr.fetchmany(5)
    #data= cr.fetchone()
    print(data)

    for i in data:
        print(i)

except Exception as e:
    print(e)

