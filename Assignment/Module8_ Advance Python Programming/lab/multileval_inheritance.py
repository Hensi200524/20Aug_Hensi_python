# Multilevel Inheritance
class Grandparent:
    def grand_info(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def parent_info(self):
        print("This is Parent class")

class Child(Parent):
    def child_info(self):
        print("This is Child class")

# Create object of Child
obj = Child()
obj.grand_info()
obj.parent_info()
obj.child_info()
