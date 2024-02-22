# Function to calculate GPA based on weighted scores
def calculate_gpa(quiz1_marks, mid_sem_marks, quiz2_marks, end_sem_marks):
    # Computing weighted scores for each exam
    quiz1_score = (quiz1_marks / 20) * 10
    mid_sem_score = (mid_sem_marks / 50) * 30
    quiz2_score = (quiz2_marks / 20) * 10
    end_sem_score = (end_sem_marks / 100) * 50

    # Computing overall weighted score
    weighted_score = quiz1_score + mid_sem_score + quiz2_score + end_sem_score

    # Computing overall GPA
    gpa = (weighted_score / 10)

    return gpa

# Function to assign grade based on GPA
def assign_grade(gpa):
    if gpa >= 10:
        return 'O'
    elif gpa >= 9:
        return 'A'
    elif gpa >= 8:
        return 'B'
    elif gpa >= 7:
        return 'C'
    elif gpa >= 6:
        return 'D'
    elif gpa >= 5:
        return 'Pass'
    else:
        return 'Fail'

# Menu-driven program
while True:
    print("\n\tMenu:")
    print("(A) Compute GPA")
    print("(B) Assign Grade")
    print("(Q) Quit")

    choice = input("Enter your choice (A/B/Q): ")

    if choice == 'A':
        # Reading marks of all 4 exams
        marks = input("Enter marks obtained in Quiz 1, Mid Sem, Quiz 2, and End Sem, separated by spaces: ").split()

        # Converting marks to float
        marks = list(map(float, marks))

        # Checking if marks are within the maximum limit
        if any(mark > max_marks for mark, max_marks in zip(marks, [20, 50, 20, 100])):
            print("Invalid marks entered. Marks should not exceed maximum limit.")
            continue

        # Computing GPA
        gpa = calculate_gpa(*marks)

        # Displaying the result
        print("Overall GPA: {:.2f}".format(gpa))

    elif choice == 'B':
        # Reading GPA from user
        gpa = float(input("Enter GPA: "))

        # Assigning grade
        grade = assign_grade(gpa)

        # Displaying the result
        print("Grade: {}".format(grade))

    elif choice == 'Q':
        # Exiting the program
        print("Exiting the program.")
        break

    else:
        # Invalid choice entered
        print("Invalid choice. Please enter A, B, or Q.") 
