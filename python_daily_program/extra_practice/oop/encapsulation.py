class student:
    def __init__(self,name,marks):
        self.name = name 
        self.__marks = marks  # private attribute hidden
        
    def get_marks(self):
            return self.__marks
        
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks = marks
        else:
            print("Invalid marks")

s1 = student("Hensi",85)
print(s1.get_marks())
#s1.set_marks(110)
s1.set_marks(98)
print(s1.get_marks())
        