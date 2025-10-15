# Banking System using Multilevel Inheritance (without main block)

class AccountOpen:
    def getdata(self):
        self.num = input("Enter your account number: ")
        self.name = input("Enter your name: ")
        self.type = input("Enter your account type (Saving/Current): ")
        self.bal = float(input("Enter your opening balance: "))

    def showdata(self):
        print("\n----- Account Details -----")
        print(f"Account No.: {self.num}")
        print(f"Name       : {self.name}")
        print(f"Type       : {self.type}")
        print(f"Balance    : ₹{self.bal}")


class Deposit(AccountOpen):
    def deposit(self):
        amt = float(input("\nEnter amount to deposit: ₹"))
        self.bal += amt
        print(f"₹{amt} deposited successfully!")
        print(f"Updated Balance: ₹{self.bal}")


class Withdraw(Deposit):
    def withdraw(self):
        amt = float(input("\nEnter amount to withdraw: ₹"))
        if amt <= self.bal:
            self.bal -= amt
            print(f"₹{amt} withdrawn successfully!")
        else:
            print("Insufficient balance!")
        print(f"Available Balance: ₹{self.bal}")


# -------- Program Execution --------
obj = Withdraw()
obj.getdata()
obj.showdata()
obj.deposit()
obj.withdraw()
obj.showdata()
