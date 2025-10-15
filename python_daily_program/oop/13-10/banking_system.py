class AccountOpen:
    def getdata(self):
        self.num = input("Enter your account number: ")
        self.name = input("Enter your name: ")
        self.type = input("Enter your account type (Saving/Current): ")
        self.bal = float(input("Enter your opening balance (Minimum ₹20000): "))
        if self.bal < 20000:
            print("Account not opened.")
            self.bal = 0
        else:
            print("Account opened successfully!")

    def showdata(self):
        print("\n----- Account Details -----")
        print(f"Account No.: {self.num}")
        print(f"Name       : {self.name}")
        print(f"Type       : {self.type}")
        print(f"Balance    : ₹{self.bal}")


class Deposit(AccountOpen):
    def deposit(self):
        if self.bal == 0:
            print("Cannot deposit.")
            return self.bal
        amt = float(input("\nEnter amount to deposit: ₹"))
        self.bal += amt
        print(f"₹{amt} deposited successfully!")
        return self.bal


class Withdraw(Deposit):
    def withdraw(self):
        if self.bal == 0:
            print("Cannot withdraw.")
            return self.bal

        amt = float(input("\nEnter amount to withdraw: ₹"))
        # Check after withdrawal, balance should not go below 20000
        if amt <= self.bal and (self.bal - amt) >= 20000:
            self.bal -= amt
            print(f"₹{amt} withdrawn successfully!")
        elif amt > self.bal:
            print("Insufficient balance!")
        else:
            print(" Withdrawal would reduce balance below ₹20000. Not allowed.")
        return self.bal


# -------- Program Execution --------
obj = Withdraw()
obj.getdata()

if obj.bal >= 20000:   # Only continue if account was opened successfully
    obj.showdata()
    new_bal = obj.deposit()
    print(f"👉 Updated Balance after deposit: ₹{new_bal}")

    new_bal = obj.withdraw()
    print(f"👉 Updated Balance after withdraw: ₹{new_bal}")

    obj.showdata()
