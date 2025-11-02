import re

mystr = "This Is python789798798"

#x = re.findall('\w',mystr)
#x = re.findall('\W',mystr)
#x = re.findall('\d',mystr)
#x = re.findall('\D',mystr)
#x = re.findall('\s',mystr)
#x = re.findall('\S',mystr)
#x = re.findall(r'\bThis',mystr)
x = re.findall('\BThis',mystr)
print(x)