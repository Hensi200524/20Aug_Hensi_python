class Employee:
    def show(self, name, salary):
        print("Employee Name:", name)
        print("Salary:", salary)

class Manager(Employee):
    # Overriding the parent method
   def show(self, name, salary):
        print("Manager Name:", name)
        print("Manager Salary:", salary + 5000)  # Bonus added



name = input("Enter your name:")
salary = int(input("Enter your salary:"))

# Create objects
e = Employee()
e.show(name, salary)

m = Manager()
m.show(name, salary)
