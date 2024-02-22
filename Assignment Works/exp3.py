 

#Q2

# Reading radius of a circle and side of a square from user using single input() method
radius, side = input("Enter radius of circle and side of square separated by a space: ").split()

# Converting the inputs from string to float
radius = float(radius)
side = float(side)

# Calculating area of the circle and the square
area_circle = 3.14159 * radius ** 2
area_square = side ** 2

# Displaying the results
print("Area of circle: {:.2f}".format(area_circle))
print("Area of square: {:.2f}".format(area_square))

#Q3
# Reading marks obtained by the student in all 6 exams
quiz1_marks, mid_sem_marks, quiz2_marks, end_sem_marks = map(float, input("Enter marks obtained in Quiz 1, Mid Sem, Quiz 2, and End Sem, separated by spaces: ").split())

# Computing weighted scores for each exam
quiz1_score = (quiz1_marks / 20) * 10
mid_sem_score = (mid_sem_marks / 50) * 30
quiz2_score = (quiz2_marks / 20) * 10
end_sem_score = (end_sem_marks / 100) * 50

# Computing overall weighted score
weighted_score = quiz1_score + mid_sem_score + quiz2_score + end_sem_score

# Computing overall GPA
gpa = (weighted_score / 10)

# Displaying the result
print("Overall GPA: {:.2f}".format(gpa))


#Q4
# Reading the year from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True")
else:
    print("False")



#Q5{Need To Modify it}
# Function to compute GPA from marks
def compute_gpa(marks):
    quiz1, mid_sem, quiz2, end_sem = marks[0], marks[1], marks[2], marks[3]
    gpa = ((quiz1/20)*0.1 + (mid_sem/50)*0.3 + (quiz2/20)*0.1 + (end_sem/100)*0.5) * 10
    return round(gpa, 2)

# Function to assign grade based on GPA
def assign_grade(gpa):
    if gpa >= 10:
        return "O"
    elif gpa >= 9:
        return "A"
    elif gpa >= 8:
        return "B"
    elif gpa >= 7:
        return "C"
    elif gpa >= 6:
        return "D"
    elif gpa >= 5:
        return "Pass"
    else:
        return "Fail"

# Menu-driven program
while True:
    print("Menu:")
    print("(A) Compute GPA")
    print("(B) Assign Grade")
    print("(Q) Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "A":
        # Reading marks from user and computing GPA
        marks = input("Enter marks of all 6 exams separated by a space: ").split()
        marks = [int(m) for m in marks]
        if max(marks) > 100:
            print("Error: Marks cannot exceed maximum marks")
            continue
        gpa = compute_gpa(marks)
        print("GPA:", gpa)
        
    elif choice == "B":
        # Reading GPA from user and assigning grade
        gpa = float(input("Enter GPA: "))
        grade = assign_grade(gpa)
        print("Grade:", grade)
        
    elif choice == "Q":
        # Quitting the program
        break
    
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")



#Q6
rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(i-1, -1, -1):
        print(2**j, end=" ")
    print()
