#email_patteren 

import re

email = input("Enter your email: ")

e_pattern = r"^[a-z0-9._]+@[a-z]+\.[a-z]{2,3}$"

if re.match(e_pattern, email):
    print("Email is correct!")
else:
    print("Error!")
