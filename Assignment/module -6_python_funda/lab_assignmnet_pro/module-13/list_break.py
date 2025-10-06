""" Write a Python program to stop the loop once 'banana' is found using
the break statement."""

list = ['apple','banana','mango','orange']

for fruit in list:
    if fruit == 'banana':
        break
    print(fruit)