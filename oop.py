#Write a python progrma to perform arthemetic caclulation
class Arthemetic:
    a=1
    b=19

    def addition(self):
        print(self.a+self.b)

    def subtraction(self):
        print(self.a-self.b)

    def multi(self):
        print(self.a*self.b)

    def divide(self):
        print(f"{(self.a/self.b):.2f}")

#
d=Arthemetic()
d.addition()
d.subtraction()
d.multi()
d.divide()
