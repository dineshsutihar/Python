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