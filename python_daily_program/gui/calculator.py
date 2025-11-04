import tkinter

tk = tkinter.Tk()
tk.title("Calculator")
tk.geometry("500x500")

lbl1 = tkinter.Label(text = "no1:",bg='lightblue',fg='black',font='verdana 15 bold')
lbl1.grid(row=0,column=0,sticky='w')

lbl2 = tkinter.Label(text = "no2:",bg='lightblue',fg='black',font='verdana 15 bold')
lbl2.grid(row=1,column=0,sticky='w')

txt1 = tkinter.Entry(bg='lightblue')
txt1.grid(row=0,column=1,sticky='w')

txt2 = tkinter.Entry(bg='lightblue')
txt2.grid(row=1,column=1,sticky='w')

def btnclick1():
    no1=txt1.get()
    no2=txt2.get()
    no3=int(no1)+int(no2)
    print("answer is :",no3)

def btnclick2():
    no1=txt1.get()
    no2=txt2.get()
    no3=int(no1)-int(no2)
    print("answer is :",no3)

def btnclick3():
    no1=txt1.get()
    no2=txt2.get()
    no3=int(no1)*int(no2)
    print("answer is :",no3)

def btnclick4():
    no1=txt1.get()
    no2=txt2.get()
    no3=int(no1)/int(no2)
    print("answer is :",no3)


btn1=tkinter.Button(text="+",bg='black',fg='red',font='verdana 15 bold',command=btnclick1) 
btn1.place(x=80,y=100)

btn2=tkinter.Button(text="-",bg='black',fg='red',font='verdana 15 bold',command=btnclick2) 
btn2.place(x=130,y=100)

btn3=tkinter.Button(text="*",bg='black',fg='red',font='verdana 15 bold',command=btnclick3) 
btn3.place(x=180,y=100)

btn4=tkinter.Button(text="/",bg='black',fg='red',font='verdana 15 bold',command=btnclick4) 
btn4.place(x=230,y=100)



tk.mainloop()

