
file = open("demofile.txt", "a")

n = int(input("how many number of students: "))

for i in range(n):
    id = input("Enter your id: ")
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    file.write(f"id :{id},name: {name},city: {city}\n-------------------------\n")

file.close()