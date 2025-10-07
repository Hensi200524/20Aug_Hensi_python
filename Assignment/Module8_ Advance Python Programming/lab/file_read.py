"""Write a Python program to read the contents of a file and print them on the console."""

file = open("myfile.txt","r")

content = file.read()

print("file content is :\n",content)
file.close()
