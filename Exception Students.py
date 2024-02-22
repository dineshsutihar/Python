#to get Usn no and Name from the user

def main():
    try:
        name=input("Enter Your name : ")
        
        
        usn=int(input("Enter Your USN Number: "))
    except:
        print("Error")
    else:
        print(f"Name of Student is {name}")
        print(f"USN is {usn}")
main()