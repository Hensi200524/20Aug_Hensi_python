#Student registration form with proper validations using nested if else


print("----------Student registration Form ---------------")
name = input("Enter your name :  ")

#check name 
if name.isalpha():
    email = input("Enter your email :")

    #check email
    if email.islower() and "@" in email and email.endswith(".com"):
        password  = input("Enter your Password : ")

        #check password
        if len(password) >= 6 and any(ch.isdigit() for ch in password) and any(ch.isalpha() for ch in password):
            c_pass = input("Enter your Confirm Password : ")

            #check confirm password
            if c_pass == password:
                m_no = input("Enter your Mobile Number :")

                #check Mobile no 
                if m_no.isdigit() and len(m_no) == 10:
                    print("\n =====Registration successfully=====")
                    print(f"your Name is : {name}")
                    print(f"your Email is : {email}")
                    print(f"your Mobile Number is : {m_no}")
                else:
                    print("Mobile number must be digits only and 10 characters long.")
            else:
                print("Password and Confirm Password do not match.")
        else:
            print("Password must be at least 6 characters long and contain both letters & digits.")
    else:
        print("Email must be in lowercase and valid (contain '@' and end with .com).")
else:
    print("Name must contain alphabets only.")