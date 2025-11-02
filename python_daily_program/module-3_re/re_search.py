import re 

data = "hello,i am hensi vaghela"

x = re.search("is",data) #returns a match object if found else None
print(x)

if x is not None:
    print("Yes, we have a match!")