#print seprate odd and even number bethween 1 to 50

"""print("Odd and Even numbers between 1 and 50 are:")

print("\n")

print("Odd numbers:")
for i in range(1,51,2):
    print(i,end = ",")

print("\n")

print("Even numbers:")
for i in range(2,51,2):
    print(i,end = ",")"""


print("odd numbers between 1 and 50 are:")
for i in range(1,51):
    if i%2 != 0:
        print(i,end = ",")
print("\n")
print("even numbers between 1 and 50 are:")     
for i in range(1,51):
    if i%2 == 0:
        print(i,end = ",")