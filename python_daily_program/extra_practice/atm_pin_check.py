#check ATM pin using while loop

correct_pin = 2242
attempt = 0 
max_attempts = 5
card_blocked = False
while attempt < max_attempts:
    pin = int(input("Enter your ATM pin :"))
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempt += 1
        if attempt < max_attempts:
            print(f"Wrong pin, you have {max_attempts - attempt} attempts left. Please try again.")
        else:
            card_blocked = True
if card_blocked:
    print("Card Blocked")
