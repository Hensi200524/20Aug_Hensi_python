"""Write a Python program to demonstrate the use of local and
global variables in a class."""

# Global variable
x = 10

class Demo:
    def show(self):
        # Local variable
        y = 20
        print("Inside the method:")
        print("Global variable x =", x)   # Accessing global variable
        print("Local variable y =", y)    # Accessing local variable

# Create object
d = Demo()
d.show()

print("\nOutside the class:")
print("Global variable x =", x)  # Global variable can be accessed anywhere
