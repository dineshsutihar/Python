#
# Example file for HelloWorld
#

def main():
    print("Hello World")
    name=input("Whats is your name? ")
    print("Nice to meet you,", name)


#this is just not to run if the program is called in another program as module.
if __name__=="__main__":
    main()