# Function to add two numbers
def add(a,b):
    return a+b

# Function to subtract two numbers
def subtract(a,b):
    return a-b

# Function to multiply two numbers
def multiply(a,b):
    return a*b

# Function to divide two numbers
def divide(a,b):
    if b!= 0:
        return a / b
    else:
        return "Error! Division by zero."

# Main calculator loop
while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
