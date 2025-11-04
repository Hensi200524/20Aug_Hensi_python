import re 

m_no = int(input("Enter a Mobile Number :"))

pattern = r'^[0-9]{10}$'

if re.match(pattern,m_no):
    print("correct Mobile Number")
else:
    print("Invalid Number")