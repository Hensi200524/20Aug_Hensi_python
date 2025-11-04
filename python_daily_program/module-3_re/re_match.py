#match at the beginning of the string
import re 

data = "hello,i am hensi vaghela"

x = re.match("hello",data) #returns a match object if found else None
print(x)

if x:
    print("Yes, we have a match!")
else:
    print("No match")