"""Write a Python program to open a file in write mode, write some text, and then close it."""

file = open("myfile.txt","w")

file.write("Hello,this is my first file handling program in python.\n")
file.write("I am learning python file handling.\n")
file.close()