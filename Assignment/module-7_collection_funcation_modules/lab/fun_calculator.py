"""Write a Python program to create a calculator using functions."""

#addition
def add(x,y):
    return x+y

#subtraction
def subtract(x,y):
    return x-y

#multiplication
def multiply(x,y):
    return x*y

#divison
def divide(x,y):
    if y==0:
        return "Error! Division by zero."
    else:
        return x/y
    
print("===simple calculator.===")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice = input("Select operation (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")