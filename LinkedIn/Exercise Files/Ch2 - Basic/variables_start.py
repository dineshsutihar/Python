# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# re-declaring the variable works
f="abc"
print(f)


# ERROR: variables of different types cannot be combined
print("This is string"+str(123))


# Global vs. local variables in functions
def someFunction():
    #this make f as global 
    global f 
    f="def"
    print(f)

someFunction()
print(f)

del(f) #deleting | undefining the variable

