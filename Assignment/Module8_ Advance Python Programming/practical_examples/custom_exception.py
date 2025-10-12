"""Write a Python program to print custom exceptions"""

# Define a custom exception
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        # Raise custom exception
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("You are eligible!")

except InvalidAgeError as e:
    print("Custom Exception:", e)
