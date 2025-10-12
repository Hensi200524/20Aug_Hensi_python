"""Write a Python program to check the current position of the file cursor using tell()."""

# Open a file in read mode (create one first if needed)
file = open("sample.txt", "r")

# Check the initial cursor position
pos = file.tell()
print("Current cursor position:", pos)

# Read some characters from the file
data = file.read(10)
print("Data read:", data)

# Check the cursor position again
pos = file.tell()
print("Cursor position after reading:", pos)

# Close the file
file.close()
