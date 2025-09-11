#mark_grade program using nested if

s1 = int(input("Enter the marks of subject 1: "))
s2 = int(input("Enter the marks of subject 2:"))
s3 = int(input("Enter the marks of subject 3: "))
s4 = int(input("Enter the marks of subject 4: "))

# if s1<40 or s2<40 or s3<40 or s4<40:
#     print("You are failed")
# else:
#     total = s1+s2+s3+s4
#     print("Total marks:",total)
#     pr = total /4
#     print("Percentage:",pr)
#     if(pr>=70):
#         print("result:A+")
#     elif(pr>=60):
#         print("result:A")
#     elif(pr>=50):
#         print("result:B")
#     elif(pr>=40):
#         print("result:C")
#     else:
#         print("You are failed")

if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    total = s1+s2+s3+s4
    print("Total marks:",total)
    pr = total /4
    print("Percentage:",pr)
    if(pr>=70):
        print("result:A+")
    elif(pr>=60):
        print("result:A")
    elif(pr>=50):
        print("result:B")
    elif(pr>=40):
        print("result:C")
    else:
        print("You are failed")
