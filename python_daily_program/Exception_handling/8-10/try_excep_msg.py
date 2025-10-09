#exception msg

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    #print("Sum:", a + b)
    print("Sum:", A + b)
except Exception as e:
    print("Error:", e) # This will print the specific error message