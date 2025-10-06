"""#implicit type casting
a = 7
b = 15.5
print(a+b)

#Explicit type casting
a = float(12)
b = int(7.8)
print(a)
print(b)"""

a = int("100") #string ->int
print(a+20, type(a)) #20 int

b = int(3.99) #float ->int
print(b,type(b)) #3 int

c = float(5) #int ->float
print(c,type(c)) #5.0

d = str(123) #int ->string
print(d + "456",type(d)) #123456

e = chr(65) #int ->char
print(e)

#bool conversion
print(int(True)) #1
print(int(False)) #0

#unicode conversion
print(ord('a')) #decimal number print 

#octal,hexadecimal,and binary conversion
print(oct(10))
print(bin(10))
print(hex(10))