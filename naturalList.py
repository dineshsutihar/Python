l=[1,2,3,4,5,6,7,8,9,10]
for x in l:
    if x%2==0:
        print(x)

#prime Numbers
numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = []

for num in numbers:
    if num > 0 and all(num % i != 0 for i in range(2, num)):
        primes.append(num)

print(primes)
#Alternative
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = []

for num in numbers:
    if num >= 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print(primes)
