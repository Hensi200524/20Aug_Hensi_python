#sum of First N number

n = int(input("Enter any number :"))
total = 0

for i in range (1,n+1):
    total += i
    print("Sum of this number is : ",total)
