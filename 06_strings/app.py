# Enhanced Sudent Grade Tracker Solution 

print("="*50)
print("         Enhanced Sudent Grade Tracker Solution")


# Student ID 
student_id_valid = False

while not student_id_valid:
    student_id = input("Enter ID: ")
    # check for positve number & non-alphabet (-101)
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please Enter Positive Numbers Only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("zero not allowed")
    else:
        print("enter numbers only")

print(student_id)