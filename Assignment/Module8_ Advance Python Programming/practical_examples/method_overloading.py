class Area:
    def find_area(self, a=None, b=None): #none as default value
        if a != None and b != None:
            print("Rectangle area:", a * b)
        elif a != None:
            print("Square area:", a * a)
        else:
            print("No value given")

obj = Area()
obj.find_area(5) # Square area
obj.find_area(5, 10) # Rectangle area
obj.find_area() # No value given
