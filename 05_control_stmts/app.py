# Student Grade Tracker Solution

# -> Student ID -> Student Name -> Attendance 
student_id = input("Enter your ID: ")
student_name = input("Enter your Name: ")
student_attendance = input("Enter your Attendance: ")

total_score = 0
number_of_scores = 0

continue_input = "yes"

while continue_input == "yes":
    current_score = int(input(f"Enter Score : {number_of_scores} "))
    continue_input = input("Do you want to continue (yes/no)? ")
    number_of_scores+=1
    # update the total score by adding current given score 
    total_score = total_score + current_score

print(number_of_scores)
print(total_score)

