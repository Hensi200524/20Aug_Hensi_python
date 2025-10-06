correct_pin = 2242
attempt = 0 

while attempt < 5:
    pin = int(input("Enter your ATM pin :"))
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("wrong pin , please try again ")
        attempt+=1
else:
    print("Card Blocked")
 