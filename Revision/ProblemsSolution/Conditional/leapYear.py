# Leap year are divisible by 4, but not by 100 unless also divisible by 400


year = 2024

if (year%4 ==0 and year % 100 != 0) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")