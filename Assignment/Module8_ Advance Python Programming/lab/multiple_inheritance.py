# Multiple Inheritance
class Father:
    def father_info(self):
        print("This is Father class")

class Mother:
    def mother_info(self):
        print("This is Mother class")

class Child(Father, Mother):
    def child_info(self):
        print("This is Child class")

# Create object of Child
obj = Child()
obj.father_info()
obj.mother_info()
obj.child_info()
