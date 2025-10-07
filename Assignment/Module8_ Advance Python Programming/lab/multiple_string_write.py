"""Write a Python program to write multiple strings into a file."""

"""file = open("newfile.txt","w")

file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")    
file.write("And this is the third line.\n")
file.close()"""

# List of strings
lines = [
    "Line 1: Python is fun.\n",
    "Line 2: File handling is easy.\n",
    "Line 3: Always close the file.\n"
]

# Open the file in write mode
with open("newfile.txt", "w") as file:
    file.writelines(lines)

print("Multiple strings written successfully using writelines()!")
