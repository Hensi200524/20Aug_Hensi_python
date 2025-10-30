class student:
    #method overloading
    def getdata(self,id,name):
        print("ID :",id)
        print("Name :",name)

    def getdata(self,id, name, age):
        print("ID :",id)
        print("Name :",name)
        print("Age :",age)  

st = student()
#st.getdata(1,"Hensi")  # This will cause an error
st.getdata(1,"Hensi",21)  
    
