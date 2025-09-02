#swapping of two number

a = 67
b = 54

print("Before Swapping")
print("a=",a)
print("b=",b)

#method 1 : using third variable

'''temp = a
a = b
b = temp'''

#method 2 : without using third variable

a,b=b,a

print("After Swapping")
print("a=",a)
print("b=",b)
