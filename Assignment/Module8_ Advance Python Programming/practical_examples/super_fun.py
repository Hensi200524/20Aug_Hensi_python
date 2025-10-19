# Demonstration of super() in inheritance

class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        # Call parent class method using super()
        super().show()
        print("This is the Child class")

# Create object of Child class
obj = Child()
obj.show()
