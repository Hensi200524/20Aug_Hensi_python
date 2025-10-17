#Grade Management system


def cal_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'

# Function to add a student
def add_stud(students):
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    grade = cal_grade(marks)
    students[name] = {'marks': marks, 'grade': grade}
    print(f"Student {name} added with grade {grade}.")

# Function to display all students
def display_stud(students):
    if not students:
        print("No students added yet.")
        return
    print("\nStudent Records:")
    print("Name\tMarks\tGrade")
    for name, info in students.items():
        print(f"{name}\t{info['marks']}\t{info['grade']}")

# Main program
students = {}

while True:
    print("\n--- Grade Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_stud(students)
    elif choice == '2':
        display_stud(students)
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
