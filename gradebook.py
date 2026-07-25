#Student Gradebook Manager
#Author : Xayan Kyle Lovell 
#Python Essentials 1 

#Returns the average of a list of marks, or None if the list is empty 
def calculate_average(marks):
    pass
#Returns the highest and lowest mark as a tuple: (highest, lowest)
def highest_and_lowest(marks):
    pass
#Asks for a mark, validate it with try-except, returns the float or None
def read_valid_mark():
    pass
#Adds a new student to the gradebook dictionary 
def add_student(gradebook):
    full_name = input("enter the students full name : ")
    gradebook[full_name] = []
#Adds one validated mark to an existing student
def add_mark(gradebook):
    pass
#Prints every student with marks and average 
def view_all(gradebook):
    pass
#Prints one student's full summary 
def student_summary(gradebook):
    pass
#Prints class statistics including pass/fail lists
def class_statistics(gradebook):
    pass
#Removes a student after y/n confirmation 
def remove_student(gradebook):
    pass

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
        print("You chose add mark")
    elif choice == "3":
        print("You chose view all students")
    elif choice == "4":
        print("You chose student summary")
    elif choice == "5":
        print("You chose class statistics")
    elif choice == "6":
        print("You chose remove a student")
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")


