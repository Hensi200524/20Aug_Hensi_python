#program to check if a person is eligible to donate blood using a nested if.

age = int(input("Enter your age : "))

if (age >=18):
    weight = float(input("Enter your weight : "))
    if (weight >= 50):
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood because you weigh less than 50 kg.")
else:
    print("You are not eligible to donate blood because you are under 18.")
