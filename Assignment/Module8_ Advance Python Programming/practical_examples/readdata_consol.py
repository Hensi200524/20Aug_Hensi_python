""" Write a Python program to read a file and print the data on the console"""

file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()