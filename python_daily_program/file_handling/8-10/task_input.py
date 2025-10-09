import random
import datetime

file=open("stdata.txt","a")

n=int(input("Enter number of students:"))

for i in range(n):
    at=datetime.datetime.now()
    id=random.randint(1111,9999)
    nm=input("Enter a Name:")
    ct=input("Enter your City:")
    
    file.write(f"Created_at:{at}\nID:{id}\nName:{nm}\nCity:{ct}\n------------\n")