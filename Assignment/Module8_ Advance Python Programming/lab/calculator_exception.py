"""Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
input)"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please enter numbers only."
    else:
        return f"The result is: {result}"
    
# Example usage
print(divide_numbers(10, 2))  # Valid input
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, 'a'))  # Invalid input type