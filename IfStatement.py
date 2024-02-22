purchase=eval(input("Enter your purchase amount"))
if(purchase>=2000):
    purchase=purchase-500
print("Amount to pay ",purchase)

print("-----------------------------------")

#Program to check age eligilibility for Voting
age=eval(input("Enter the age: "))
if(age>=18):
    print("you are eligable")
else:
    print("you are not eligable")

print("-----------------------------------")

#Program to check Odd and Even
n=eval(input("enter the number"))
if(n%2==0):
    print("number is even")
else:
    print("number is Odd")

print("-----------------------------------")

#positive or negative number
m=eval(input("enter the number"))
if(m<0):
    print("number is negative")
else:
    print("number is positive")

print("-----------------------------------")
#leap year or not
y=eval(input("enter the year"))
if(y%4==0):
    print(" is leap year")
else:
     print(" not leap year")

print("-----------------------------------")
#greatest of two number

g=eval(input("enter the number m: "))
h=eval(input("enter the number h: "))

if(m<h):
    print("m is less than h")
elif(m==h):
    print("m equals h")
else:
    print("m is grater than h")

print("-----------------------------------")

#to display the given values
d=eval(input("enter the number"))
c=eval(input("enter the number"))

if(d==c):
    print("Hi\nGood\nmorning")
else:
     print("END")


print("-----------------------------------")

#wap to get number from the user 1 to 7 to display the days in a week 
day=eval(input("Enter the no of days" ))
if(day==1):
    print("Sunday")
elif(day==2):
    print("Monday")
elif(day==3):
    print("tuesday")
elif(day==4):
    print("wednusday")
elif(day==5):
    print("Thrusday")
elif(day==6):
    print("Friday")
elif(day==7):
    print("Saturday")
else:
    print("\nWRONG INPUT")

print("-----------------------------------")