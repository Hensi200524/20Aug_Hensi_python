file = open("table1.py","w")


n = int(input("Enter a number :"))

for i in range(1,11):
    result = n*i
    file.write(f"{n} x {i} = {result}\n")


