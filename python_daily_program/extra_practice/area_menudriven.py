#find the area of circle,rectangle,square using menu driven.

print("========Menu========")
print("1.Area of circle")
print("2.Area of Rectangle")
print("3.Area of Square")

choice = int(input("Enter the choice:"))

if choice == 1:
    r = float(input("Enter the radius:"))
    area = 3.14*r*r
    print(f"the area of circle is : {area}")

elif choice == 2:
    l = float(input("Enter the length: "))
    b = float(input("Enter the width: "))
    area = l * b
    print(f"the area of rectangle is : {area}")

elif choice == 3:
    s = float(input("Enter the side:"))
    area = s*s
    print(f"the area of square is : {area}")

else:
    print("Invalid choice")


