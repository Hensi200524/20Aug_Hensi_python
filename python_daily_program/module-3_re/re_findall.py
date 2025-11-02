import re 

data = input("Enter your data: ")

x = re.findall("r",data) #returns a match object if found else None
print(x)

if x:
    print("Yes, we have a match!")
else:
    print("No match")