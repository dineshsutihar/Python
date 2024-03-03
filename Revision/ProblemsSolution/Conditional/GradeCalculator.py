# Assign a letter grade based on a student's score : A(90-100) B(80-89) C(70-79),D(60-69). F(below 60)

markObtained = -29
grade = 'F'

if(markObtained>100 or markObtained <0):
    print("Wrong Grading")
    exit()

if(90 <= markObtained <= 100):
    grade = 'A'
elif(80 <= markObtained <90):
    grade = 'B'
elif( 70 <= markObtained <80):
    grade = 'C'
elif( 60 <= markObtained < 70):
    grade = 'D'
else:
    grade = 'F'
    
    
print("You have obtained:", grade)