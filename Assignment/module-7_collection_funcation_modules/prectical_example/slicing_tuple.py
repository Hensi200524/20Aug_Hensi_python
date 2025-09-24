"""Slicing a tuple to access ranges of elements."""

tuple = (1,2,3,4,5,6,7,8,9) # Creating a tuple

# print(tuple[2:5]) # Accessing elements from index 2 to 4
# print(tuple[:4]) # Accessing elements from start to index 3
# print(tuple[5:]) # Accessing elements from index 5 to end
# print(tuple[-5:-2]) # Accessing elements from index -5 to -3
# print(tuple[:]) # Accessing all elements of the tuple
# print(tuple[::-1]) # Accessing all elements in reverse order
# print(tuple[::2]) # Accessing elements with a step of 2
# print(tuple[1::2]) # Accessing elements with a step of 2 starting from index 1

#---------------------------------------------------#
#Write a Python program to access values between index 1 and 5 in a tuple.

tuple = (1,2,3,4,5,6,7,8,9) 
print(tuple[1:6])

#Write a Python program to access alternate values between index 1 and 5 in a tuple.
print(tuple[1:6:2])