import re

mystr = "I am Hensi vaghela09898"

#x = re.findall('[A-Z]',mystr)
x = re.findall("H..si",mystr)
print(x)