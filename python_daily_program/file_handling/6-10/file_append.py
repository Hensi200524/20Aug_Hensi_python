file = open("newfile.txt","a")

id = int(input("Enter your id :"))
name = input("Enter your name :")

file.write(f"id := {id} and name := {name}\n")