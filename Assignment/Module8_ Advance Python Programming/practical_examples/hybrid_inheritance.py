# Hybrid Inheritance

class A:     # Base class
    def show_A(self):
        print("This is Class A")

class B(A):  # B inherits from A  (Single / Multilevel)
    def show_B(self):
        print("This is Class B (inherits A)")

class C:     # Another independent class
    def show_C(self):
        print("This is Class C")

class D(B, C):  # D inherits from both B and C (Multiple)
    def show_D(self):
        print("This is Class D (inherits B and C)")
        

# Create object of D
obj = D()
obj.show_A()   # From A through B
obj.show_B()   # From B
obj.show_C()   # From C
obj.show_D()   # From D
