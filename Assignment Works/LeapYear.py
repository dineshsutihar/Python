#Q4
# Reading the year from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True")
else:
    print("False")