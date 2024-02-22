#app open the need 4 digit pin only number 
def main():
    try:
        pin=input("Enter Your 4 Digit PIN: ")
        if pin.isdigit():
            print("Access Granted")
        else:
            raise Exception
    except Exception:
        print("Invalid PIN")
    else:
        print("Welcome to App>😊")
main()



# input_str = input("Enter a string: ")
# if input_str.isdigit():
#     print("The string contains only numbers.")
# else:
#     print("The string contains characters other than numbers.")

# #a software developer is designing an online money transfer application. when 
# #opening the app, it will ask 