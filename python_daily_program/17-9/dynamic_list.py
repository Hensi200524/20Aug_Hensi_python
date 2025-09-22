#dynaic list with user input

data = [] # empty list
n = int(input("Enter number of elements: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    data.append(element) # add element to the list
print("The list is:", data)
print("The current length of the list is:", len(data))
   