#count the number of days in given year and month
import calendar

def countdays(theyear, themonth, whichday):
    daycount=0
    weeklist=calendar.monthcalendar(theyear, themonth)
    for week in weeklist:
        if week[whichday] != 0:
            daycount+=1
    return daycount

print("--Day counter program--")
run=True
while run:
    try:
        print("Which day do you want to count?")
        print("1. Monday")
        print("2. Tuesday")
        print("3. Wednesday")
        print("4. Thursday")
        print("5. Friday")
        print("6. Saturday")
        print("7. Sunday")
        print("8. Exit")
        theday=int(input("Enter your choice: "))
        if theday==8:
            run=False
            break
        day=int(theday)
        yearstr=input("Enter the year: ")
        year=int(yearstr)
        monthstr=input("Enter the month: ")
        month=int(monthstr)

        result=countdays(year, month, day)
        print("There are", result, "days in", calendar.month_name[month], year)
        print("--"*30)
    except Exception as e:
        print(e)
        print("Please enter a valid input")
        print("--"*30)
print("Thank you for using the program")