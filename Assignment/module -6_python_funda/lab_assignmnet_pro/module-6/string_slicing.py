"""Write a Python program to demonstrate string slicing"""

str = "hello, i am hensi"

print(str[0:5])  #start index is 0 and end index is 5
print(str[7:9])  #start index is 7 and end index is 9
print(str[10:13]) #start index is 10 and end index is 13
print(str[14:])  #start index is 14 and end index is end of string
print(str[:5])  #start index is beginning of string and end index is 5
print(str[-5:])  #start index is -5 and end index is end of string
print(str[::2])  #start index is beginning of string and end index is end of string, step is 2
print(str[1::2])  #start index is 1 and end index is end of string, step is 2
print(str[::-1])  #start index is end of string and end index is beginning of string, step is -1
print(str[-1:-6:-1])  #start index is -1 and end index is -6, step is -1
print(str[-6::-1])  #start index is -6 and end index is beginning of string, step is -1
print(str[-1::-1])  #start index is -1 and end index is beginning of string, step is -144