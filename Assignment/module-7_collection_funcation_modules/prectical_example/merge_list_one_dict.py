"""Write a Python program to merge two lists into one dictionary using a loop."""

list1 = ['name', 'age', 'city'] # Creating first list
list2 = ['Hensi', 21, 'Morbi'] # Creating second list

dict = {} # Creating an empty dictionary

for i in range(len(list1)): # Iterating over the range of length of first list
    dict[list1[i]] = list2[i] # Assigning values from second list to keys from first list

print(dict) # Printing the merged dictionary