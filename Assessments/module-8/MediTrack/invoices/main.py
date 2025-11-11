import sqlite3

def init_db():
    try:
        db = sqlite3.connect("meditrack.db")
        print("Database created!")
    except Exception as e:
        print(e)
            

    # Create users table
    tbl1_create = "create table users(u_id integer primary key autoincrement,username text not null,password text not null,role text not null)"

    try:
        db.execute(tbl1_create)
        print("user table created!")
    except Exception as e:
        print(e)

    #create patients
    tbl2_create = "create table patients(p_id integer primary key autoincrement,name text not null,dob text not null,contact text,address text,history text)"

    try:
        db.execute(tbl2_create)
        print("patients table created!")
    except Exception as e:
        print(e)

    #create appointments
    tbl3_create = "create table appointments(a_id integer primary key autoincrement,patient_id integer,doctor_id integer,datetime text,reason text,status text,charges real,FOREIGN KEY(patient_id) REFERENCES patients(p_id),FOREIGN KEY(doctor_id) REFERENCES users(u_id))"

    try:
        db.execute(tbl3_create)
        print("appointments table created!")
    except Exception as e:
        print(e)

    print("Database initialized successfully!")

    #insert users 
    """add_user = "INSERT into users(username,password,role)values('Usha','123','Admin'),('Khusboo','456','doctor'),('Jenisha','785','Receptionist')"

    try:
        db.execute(add_user)
        db.commit()
        print("record inserted!")
    except Exception as e:
        print(e)"""
    
#show data
def show_data():
    try:
        db = sqlite3.connect("meditrack.db")
        print("Database created!")
    except Exception as e:
        print(e)

    cr = db.cursor()
    show_user ="Select * from users"


    try:
        cr.execute(show_user)
        data = cr.fetchall()
        for i in data:
            print(i)
        print("record show...")
    except Exception as e:
        print(e)
            
# Run this only once to create the database
init_db()
show_data()