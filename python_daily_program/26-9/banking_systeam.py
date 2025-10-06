# Multi-Account Banking System
"""
#Dictionary to store multiple accounts
accounts = {}

# Function to create account
def create_account():
    accno = input("Enter Account Number: ")
    
    if accno in accounts:
        print("\n Account number already exists!")
        return
    
    name = input("Enter Account Holder Name: ")
    acctype = input("Enter Account Type (Savings/Current): ")

    accounts[accno] = {
        "name": name,
        "acctype": acctype,
        "balance": 0
    }
    print("\n Account created successfully!")
    print_account_details(accno)

# Function to display account details
def print_account_details(accno):
    if accno in accounts:
        acc = accounts[accno]
        print("\n----- Account Details -----")
        print(f"Account No : {accno}")
        print(f"Name       : {acc['name']}")
        print(f"Acc Type   : {acc['acctype']}")
        print(f"Balance    : ₹{acc['balance']}")
    else:
        print("\n Account not found!")

# Function to check balance
def check_balance(accno):
    if accno in accounts:
        print(f"\n[{accno}] {accounts[accno]['name']}'s Balance: ₹{accounts[accno]['balance']}")
    else:
        print("\n Account not found!")

# Function to deposit money
def deposit(accno, amount):
    if accno in accounts:
        accounts[accno]["balance"] += amount
        print(f"\n₹{amount} deposited successfully in [{accno}] {accounts[accno]['name']}'s account")
        check_balance(accno)
    else:
        print("\n Account not found!")

# Function to withdraw money
def withdraw(accno, amount):
    if accno in accounts:
        if amount <= accounts[accno]["balance"]:
            accounts[accno]["balance"] -= amount
            print(f"\n₹{amount} withdrawn successfully from [{accno}] {accounts[accno]['name']}'s account")
        else:
            print("\n Insufficient balance!")
        check_balance(accno)
    else:
        print("\n Account not found!")

# Function to display menu
def menu():
    while True:
        print("\n----- Banking System -----")
        print("1. Create Account")
        print("2. Show Account Details")
        print("3. Check Balance")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            accno = input("Enter Account Number: ")
            print_account_details(accno)
        elif choice == 3:
            accno = input("Enter Account Number: ")
            check_balance(accno)
        elif choice == 4:
            accno = input("Enter Account Number: ")
            amt = int(input("Enter amount to deposit: ₹"))
            deposit(accno, amt)
        elif choice == 5:
            accno = input("Enter Account Number: ")
            amt = int(input("Enter amount to withdraw: ₹"))
            withdraw(accno, amt)
        elif choice == 6:
            print("\n Thank you for banking with us!")
            break
        else:
            print("\n Invalid choice! Please try again.")

# Run the program
menu()
"""

# Global variables     
account_number = ""
name = ""
balance = 0.0

def create_account():
    global account_number, name, balance
    account_number = input("Enter a new Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = 0.0
    print("\n Account created successfully!")
    print("Account Number:", account_number)
    print("Account Holder:", name)
    print("Current Balance: ", balance)

def deposit():
    global balance
    acc = input("Enter your Account Number: ")
    if acc == account_number:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount} deposited successfully. New balance: {balance}")
        else:
            print(" Invalid deposit amount.")
    else:
        print(" Account not found!")

def withdraw():
    global balance
    acc = input("Enter your Account Number: ")
    if acc == account_number:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print(f" ₹{amount} withdrawn successfully. Remaining balance: ₹{balance}")
        else:
            print(" Insufficient balance.")
    else:
        print(" Account not found!")

def check_balance():
    acc = input("Enter your Account Number: ")
    if acc == account_number:
        print(f" Account Holder: {name}")
        print(f" Current Balance: ₹{balance}")
    else:
        print(" Account not found!")

# --------- MAIN PROGRAM ----------
while True:
    print("\n=== SIMPLE BANKING SYSTEM ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print(" Thank you for using our bank!")
        break
    else:
        print(" Invalid choice. Try again.")