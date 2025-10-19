# Hierarchical Inheritance

class Parent:
    def show_parent(self):
        print("This is the Parent class")

class Child1(Parent):
    def show_child1(self):
        print("This is Child1 class")

class Child2(Parent):
    def show_child2(self):
        print("This is Child2 class")

# Create object of Child1
obj1 = Child1()
obj1.show_parent()
obj1.show_child1()

# Create object of Child2
obj2 = Child2()
obj2.show_parent()
obj2.show_child2()
