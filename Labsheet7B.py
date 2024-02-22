class Student:
    def __init__(self, name, usn, che, phy, maths, bio, cse):
        self.name = name
        self.usn = usn
        self.che = che
        self.phy = phy
        self.maths = maths
        self.bio = bio
        self.cse = cse

    def display(self):
        print(f"Name: {self.name}, USN: {self.usn}, Chemistry: {self.che}, Physics: {self.phy}, Maths: {self.maths}, Biology: {self.bio}, CSE: {self.cse}")

N = int(input("Enter the number of students: "))

students = []
for i in range(N):
    print()
    name = input(f"Enter the name of student {i+1}: ")
    usn = input(f"Enter the USN of student {i+1}: ")
    che = int(input(f"Enter the Chemistry marks of student {i+1}: "))
    phy = int(input(f"Enter the Physics marks of student {i+1}: "))
    maths = int(input(f"Enter the Maths marks of student {i+1}: "))
    bio = int(input(f"Enter the Biology marks of student {i+1}: "))
    cse = int(input(f"Enter the CSE marks of student {i+1}: "))
    students.append(Student(name, usn, che, phy, maths, bio, cse))
    

print("\nStudent Details:")
for student in students:
    student.display()
