"""Write a Python program to handle file exceptions and use the finally block for closing
the file."""

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("File was not opened.")
