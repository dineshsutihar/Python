# Prime : a whole number greater than 1 that cannot be divide by any number other then its self and 1

number = 30

is_prime = True

if number > 1: 
    for i in range(2,number):
        if (number % i) == 0:
            is_prime = False
            break
        
print("Number is prime?: ", is_prime)
        