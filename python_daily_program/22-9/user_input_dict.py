stdata = {}

pair = int(input("Enter how many pairs add : "))

for i in range(1,pair+1):
    key = input("Enter key : ")
    value = input("Enter value : ")
    stdata[key] = value

print(stdata)