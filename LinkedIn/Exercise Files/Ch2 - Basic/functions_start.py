#
# Example file for working with functions
#

# define a basic function
def func1():
    print("Iam a function.")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)


# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def prower(num, x=1):
    result=1
    for i in range(x):
        result=result*num
    return result

#function with variable number of arguments
def multi_add(*args):
    result=0
    for x in args:
        result +=x
        #print("X="a) 
    return result




# Calling the functions
func1() #print the Iam a function

print(func1()) # Print the above line and None because our fucntion doesnot returns anything

print(func1) # return the memory address 

func2(10,20)
print(func2(10,20))
print(cube(3))

#
print(prower(2))
print(prower(2,3))
print(prower(x=3,num=2))

#
print(multi_add(10,4,5,10,4))