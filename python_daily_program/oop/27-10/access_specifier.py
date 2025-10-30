#public access specifier

class Student:
    id = 101  # Public attribute
    name = "Hensi" # Public attribute

    def getdata(self):
        print("This is a public method")

st = Student()
print(st.id)  # Accessing public attribute
print(st.name)  # Accessing public attribute        
st.getdata()  # Calling public method