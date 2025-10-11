"""Write a Python program to demonstrate handling multiple exceptions"""

try:
    num = int(input("Enter a number: "))   # May raise ValueError
    result = 10 / num                      # May raise ZeroDivisionError
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("An unexpected error occurred:", e)

