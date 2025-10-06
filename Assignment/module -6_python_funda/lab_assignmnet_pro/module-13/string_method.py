"""Write a Python program that manipulates and prints strings using various string methods."""

str = "hello world"
print(str.upper())          # Convert to uppercase
print(str.lower())          # Convert to lowercase
print(str.capitalize())     # Capitalize first letter
print(str.title())          # Title case
print(str.strip())          # Remove leading/trailing whitespace
print(str.replace("world", "Python"))  # Replace substring
print(str.split())          # Split string into a list
print(str.find("world"))    # Find substring index
print(str.startswith("hello"))  # Check if string starts with a substring
print(str.endswith("world"))    # Check if string ends with a substring
print(str.count("o"))       # Count occurrences of a substring
print(str.isalpha())       # Check if all characters are alphabetic
print(str.isdigit())       # Check if all characters are digits
print(str.join(["Hello", "from", "Python"]))  # Join list of strings with str as separator
print(str.center(30))       # Center the string within a specified width
print(str.zfill(20))       # Pad the string with zeros on the left to fill a width
