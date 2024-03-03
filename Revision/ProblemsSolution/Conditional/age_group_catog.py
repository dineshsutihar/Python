x = int (input("Enter the age: "))

if(x<13):
    print("Child")
    
elif (x>=13 and x<=19 ):
    print("Teenager")
    
elif(x>=20 and x<=59):
    print("Adult")
else: 
    print("Senior")