"""Write a Python program to demonstrate the use of functions from
the math module."""

import math

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def factorial(n):
    return math.factorial(n)

# Example usage
num = 16
print(f"The square root of {num} is {square_root(num)}")
base = 2
exponent = 3
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
fact_num = 5
print(f"The factorial of {fact_num} is {factorial(fact_num)}")