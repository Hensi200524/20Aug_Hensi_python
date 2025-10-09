"""task: collect multipleuserinput(s) -create at(current date time) -Id(Auto generated) -name city"""

import datetime

file = open("user.txt","a")

user = int(input("How many user you want to add: "))
for i in range(1,user+1):
    print(f"\n----- User {i} -----")
    name = input("Enter name: ")
    city = input("Enter city: ")
    user_id = i
    created_at = datetime.datetime.now()
    file.write(f"ID: {user_id} | Name: {name} | City: {city} | Created At: {created_at}\n")

print("\n✅ Data saved successfully!\n")
file.close()