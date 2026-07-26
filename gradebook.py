#Student Gradebook Manager
#Author : Xayan Kyle Lovell 
#Python Essentials 1 

#Returns the average of a list of marks, or None if the list is empty 
def calculate_average(marks):
    if len(marks) == 0:
        return None
    total = sum(marks)
    average = total / len(marks)
    return average

#Returns the highest and lowest mark as a tuple: (highest, lowest)
def highest_and_lowest(marks):
    if len(marks) == 0:
        return None
    return max(marks), min(marks)

#Asks for a mark, validate it with try-except, returns the float or None
def read_valid_mark():
    while True:
        valid_mark = input("Enter a mark (0-100): ")
        try:
            valid_mark = float(valid_mark)
            if 0 <= valid_mark <= 100:
                return valid_mark
            else:
                print("Mark must be between 0-100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Adds one valid student to gradebook
def add_student(gradebook):
    full_name = input("Enter the student's full name : ")
    if full_name == "":
        print("Student name cannot be blank")
        return
    if full_name in gradebook:
        print("Student already exist.")
    else:
        gradebook[full_name] = []
        print("Student added successfully.")

#Adds one validated mark to an existing student
def add_mark(gradebook):
    full_name = input("Enter the students full name: ")
    if full_name in gradebook:
        mark = read_valid_mark()
        gradebook[full_name].append(mark)
        print("mark added successfully")
    else:
        print("student not found.")

#Prints every student with marks and average 
def view_all(gradebook):
    if len(gradebook) == 0:
        print("No students found in the gradebook.")
        return
    for student, marks in gradebook.items():
        average = calculate_average(marks)
        print(f"\nStudent: {student}")
        print(f"Marks: {marks}")
        if average is None:
            print("Average: No marks yet")
        else:
            print(f"Average: {average:.2f}")


#Prints one student's full summary 
def student_summary(gradebook):
    full_name = input("Enter the student's full name: ")
    if full_name not in gradebook:
        print("student not found.")
        return
    marks = gradebook[full_name]
    average = calculate_average(marks)
    result = highest_and_lowest(marks)
    print(f"\nStudent: {full_name}")
    print(f"Marks: {marks}")
    if average is None:
        print("No marks available")
    else:
        highest, lowest = result
        print(f"Average: {average:.2f}")
        print(f"Highest: {highest}")
        print(f"Lowest: {lowest}")

#Prints class statistics including pass/fail lists
def class_statistics(gradebook):
    if len(gradebook) == 0:
        print("No students found.")
        return
    passed = []
    failed = []
    no_marks = []
    total_marks = []
    top_student = None
    highest_average = -1
    for student, marks in gradebook.items():
        if len(marks) == 0:
            no_marks.append(student)
            continue
        average = calculate_average(marks)
        total_marks.extend(marks)
        if average >= 50:
            passed.append(student)
        else:
            failed.append(student)
        if average > highest_average:
            highest_average = average
            top_student = student
    if len(total_marks) == 0:
        print("No marks have been entered yet.")
        return
    class_average = sum(total_marks) / len(total_marks)
    print("\n===== Class Statistics =====")
    print(f"Total students: {len(gradebook)}")
    print(f"Class average: {class_average:.2f}")
    print(f"Top student: {top_student} ({highest_average:.2f})")
    print(f"Passed ({len(passed)}): {passed}")
    print(f"Failed ({len(failed)}): {failed}")
    print(f"No marks yet ({len(no_marks)}): {no_marks}")
   
#Removes a student after y/n confirmation 
def remove_student(gradebook):
    full_name = input("Enter the students full name: ")
    if full_name not in gradebook:
        print("Student not found")
        return
    confirm = input("Are you sure (y/n): ").lower()
    if confirm == "y":
        del gradebook[full_name]
        print("Student removed successfully.")
    else:
        print("Removal cancelled.")

# ---- Main Program ----

gradebook = {}

while True:
    print("\n===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. Add Mark")
    print("3. View All Students")
    print("4. Student Summary")
    print("5. Class Statistics")
    print("6. Remove a Student")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        add_student(gradebook)
        print(gradebook)
    elif choice == "2":
        add_mark(gradebook)
        print(gradebook)
    elif choice == "3":
        view_all(gradebook)
    elif choice == "4":
        student_summary(gradebook)
    elif choice == "5":
        class_statistics(gradebook)
    elif choice == "6":
        remove_student(gradebook)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

    
