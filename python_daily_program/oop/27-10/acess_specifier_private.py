class student:
    #private
    __id = 101
    __name = "Hensi"

    #public  method
    """def getdata(self):
        print("This is a public method")
        print("ID :",self.__id)
        print("Name :",self.__name)"""

    #private method
    def __getdata(self):
        print("This is a private method")
        print("ID :",self.__id)
        print("Name :",self.__name)

    def printdata(self):
        self.__getdata()

st = student()
#print("ID : ",st.__id) #error
#print("Name : ",st.__name) #error
#st.getdata()  # Calling public method  
st.printdata()      
