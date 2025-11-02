import re

mystr = "I am Hensi vaghela09898"

#x = re.findall('[A-Z]',mystr)
x = re.findall('[A-Za-z0-9]',mystr)
print(x)