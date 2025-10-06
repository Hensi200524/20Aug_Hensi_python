#max number find out
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the max number")
elif b >= a and b >= c:
    print(f"{b} is the max number")
else:
    print(f"{c} is the max number")