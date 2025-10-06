#reverse number

n = int(input("Enter any number :"))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev *10+digit
    n//=10

    print("Reverse number is : ",rev)