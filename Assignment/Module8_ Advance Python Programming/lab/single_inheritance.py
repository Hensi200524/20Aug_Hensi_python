# Single Inheritance
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

# Create object of Child
obj = Child()
obj.show_parent()
obj.show_child()
