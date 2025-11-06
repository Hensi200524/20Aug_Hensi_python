import sqlite3

try:
    db = sqlite3.connect('u_info.db')
    print("Database connected...")
except Exception as e:
    print(e)

#table created 
tbl_create = "create table user(id integer primary key autoincrement,name varchar(20),city varchar(20))"

try:
    db.execute(tbl_create)
    print("Table create successfully")
except Exception as e:
    print(e)

#insert data
"""no = int(input("Enter how many record inserted?"))
for i in range(no):
    uname= input("Enter your name :")
    ucity = input("Enter your city :")
    insert_data = "insert into user(name,city)values(?,?)"

    try:
        db.execute(insert_data,(uname,ucity))
        db.commit()#save data
        print(f" {i} Insert record successfully..")
    except Exception as e:
        print(e)"""

#update data

"""uid = input("Enter ID to update :")
uname = input("Enter name to update :")
ucity = input("Enter city to update :")
update_data = f"update user set name='{uname}',city='{ucity}' where id={uid}"
print(update_data)

try:
    db.execute(update_data)
    db.commit()#save data
    print("Update record successfully..")
except Exception as e:
    print(e)"""

#delete data
uid = input("Enter ID to delete :")
delete_data = f"delete from user where id = {uid}"

try:
    db.execute(delete_data)
    db.commit()#save data
    print("delete record successfully..")
except Exception as e:
    print(e)

#show data
"""cr = db.cursor()
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

"""