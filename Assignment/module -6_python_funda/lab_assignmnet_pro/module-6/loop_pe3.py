# Write a Python program to find a specific string in the list using a simple for loop and if condition.

list1 = ['apple', 'banana', 'mango', 'orange', 'kiwi']

search_fruit = 'mango'

for fruit in list1:
    if fruit == search_fruit:
        print(f"{search_fruit} is found in the list.")
        break
    else:
        print(f"{fruit} is not found in the list.")
     
