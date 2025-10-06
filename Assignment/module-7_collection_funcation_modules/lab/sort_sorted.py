"""Write a Python program to sort a list using both sort() and sorted()."""

list = [4,2,1,3,2,7,6] # Creating a list of unsorted numbers

list.sort() # Sorting the list using sort() method
print("Sorted list using sort(): ", list)

"""sorted_list = sorted(list) # Sorting the list using sorted() function
print("Sorted list using sorted(): ", sorted_list)"""

print("Sorted list using sorted(): ", sorted(list)) # Sorting and printing the list using sorted() function