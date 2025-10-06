myset = set() # empty set

n = int(input("Enter number of elements in set: "))

for i in range(n):
    element = input("Enter element: ")
    myset.add(element)
    #myset.update([element])    
print("Set elements are: ", myset)