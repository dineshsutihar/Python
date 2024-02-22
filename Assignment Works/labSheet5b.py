# Mr. Rohit, a student of CSE department, has the assignment multiplying two complex numbers, 
# but hw did not know the concept of multiplying two complex number, So, you need to help him to solve 
# using overloading concept in Python to complete his task, Write the correct code.
# 1. get two complex number form user 
# 2. Apply overloading using magic method
# 3. Multiplicarion  two complex number
# 4. Display number
class ComplexNumber:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __mul__(self, U):  # Now, we will multiply the two objects
        real_part = (self.X * U.X) - (self.Y * U.Y)
        imaginary_part = (self.X * U.Y) + (self.Y * U.X)
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        return f"Complex Number is {self.X} + {self.Y}i"


i1, j1= input("Enter the real and imagenary part seperated by space : ").split()
i2, j2= input("Enter the real and imagenary part: seperated by space: ").split()

i1=int(i1)
j1=int(j1)

i2=int(i2)
j2=int(j2)


Object_1 = ComplexNumber(i1, j1)
Object_2 = ComplexNumber(i2, j2)
Object_3 = Object_1 * Object_2  # Multiplication using the "*" operator
print(Object_3)
