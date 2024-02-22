#wap to find year is leap year or not year divide by 4 100 and 400
class LeapYear:
    def __init__(self,year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("True")
        else:
            print("False")

year = int(input("Enter a year: "))
y=LeapYear(year)
