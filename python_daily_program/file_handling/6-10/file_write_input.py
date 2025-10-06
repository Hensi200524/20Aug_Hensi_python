file = open("temp.txt","w")

name = input("Enter your name :")
marks = int(input("Enter the marks:"))

file.write(f"your name is {name} and your marks is {marks}")