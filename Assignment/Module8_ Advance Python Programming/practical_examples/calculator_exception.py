"""Write a Python program to handle exceptions in a calculator"""

a = int(input("Enter number 1 :"))
b = int(input("Enter number 2:"))
op = input("Enter operator (+, -, *, /): ")
try:
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Thank you for using the calculator.")