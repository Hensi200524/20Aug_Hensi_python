
import tkinter
import pymysql

try:
    db = pymysql.connect(host='localhost',user='root',password='',database='pydb')
    print("Database connected!")
except Exception as e:
    print(e)

tk=tkinter.Tk()
tk.title("sqlApp")
tk.geometry("500x500")
tk.config(background="lightblue")

lbl1=tkinter.Label(text="name",bg='lightblue',fg='Black',font=("Arial", 18, "bold"))
#lbl1.pack()
#lbl1.place(x=0,y=0)
lbl1.grid(row=0,column=0,sticky='w')

lbl2=tkinter.Label(text="city",bg='lightblue',fg='Black',font=("Arial", 18, "bold"))
#lbl2.pack()
#lbl2.place(x=0,y=30)
lbl2.grid(row=1,column=0,sticky='w')

txt1=tkinter.Entry()
#txt1.place(x=100,y=0)
txt1.grid(row=0,column=1,sticky='w')

txt2=tkinter.Entry()
txt2.grid(row=1,column=1,sticky='w')

cr=db.cursor()

def btnClick():
    name =txt1.get()
    city = txt2.get()
    print(name,city)
    
    insert_data = f"insert into studinfo(name,city)values('{name}','{city}')"
    try:
        cr.execute(insert_data)
        db.commit()#save data
        print("Insert record successfully..")
    except Exception as e:
        print(e)

btn=tkinter.Button(text="Save",fg='black',font=("Arial", 12, "bold"),command=btnClick)
btn.place(x=170,y=250)
tk.mainloop()
