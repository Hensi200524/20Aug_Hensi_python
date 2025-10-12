"""Write a Python program to handle multiple exceptions (e.g., file not found, division by zero)."""

try:
    # Attempt to open a file
    file = open("newfile.txt", "r")
    data = file.read()

    # Perform a division operation
    result = 100 / 0
    print("Result:", result)

except FileNotFoundError:
    print("Error: The file was not found.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid data in the file.")

finally:
    # This will run whether an exception occurs or not
    try:
        file.close()
    except NameError:
        pass
    print("Execution completed.")
