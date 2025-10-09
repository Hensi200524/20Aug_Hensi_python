try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except:
    print("Error")
finally: # this block will always execute
    print("This is Finally block!")