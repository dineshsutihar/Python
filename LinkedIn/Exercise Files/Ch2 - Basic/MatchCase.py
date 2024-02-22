#Match case is simillar to the switch case fo C++ or Java
#It is used to match the case of the input string to the case of the string in the list
#example
def main():
    string="Hello"
    match string:
        case "Hi":
            print("Hi")
        case "Hlw": 
            print("Hlw")
        case "Hello":
            print("Hello")
        case "Hello World":
            print("Hello World")
        case _:
            print("No match found")

if __name__ == "__main__":
    main()