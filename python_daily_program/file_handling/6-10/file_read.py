file = open("table1.py","r")

#print(file.read()) #read all the data
#print(file.readline()) #read only first line
#print(file.readlines()) #read all the lines and store in list
print(file.readlines()[2]) #read all the lines and store in list and print only 3rd line
