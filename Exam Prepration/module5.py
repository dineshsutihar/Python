#code for Array creation 
import numpy as np
a=np.array([1,2,3,4,5,6,7,6])
print(a)
zero=np.zeros((2,3))
print(zero)
one=np.ones((3,4))
print(one)
print(np.empty((2,3)))

#manupulation
a=np.arange(1,9)
print(a)
print(np.reshape(a,(2,4)))
print(a.reshape(4,2))

#transpose
a=np.ones((2,3))
print(a)
print(a.T)

#mathematical calculation
a=np.arange(1,15)
print(a)
print(np.sum(a))
b=np.arange(1,15)
print(b)
#add
print(np.add(a,b))
#subtract
print(np.subtract(a,b))
#multiply
print(np.multiply(a,b))
#sqrt
print(np.sqrt(a))
#exp
print(np.exp(a))
#power
print(np.power(a,2))

#statistical calculation
a=np.arange(1,15)
print(a)
print(np.mean(a)) #mean
print(np.median(a)) #median
print(np.std(a)) #standard deviation
print(np.var(a)) #variance
print(np.min(a)) #minimum
print(np.max(a)) #maximum
print(np.argmin(a)) #index of minimum
print(np.argmax(a)) #index of maximum


#dot product
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a.dot(b))

#all the cases like upper,lower,swapcase, title, capitalize using numpy
a=np.array(["hello","world","python"])
print(a)
print(np.char.upper(a))
print(np.char.lower(a))
print(np.char.swapcase(a))
print(np.char.title(a))
print(np.char.capitalize(a))

a="Hello World"
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
print(a.capitalize())

#adding and deleting elements form the numpy array
a=np.arange(1,10)
b=np.arange(11,20)
print(a)
print(b)
print(np.append(a,b))
print(np.delete(a,2)) #delete the element at index 2
print(np.delete(a,[2,3,4])) #delete the elements at index 2,3,4

#axis
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a)
print(np.sum(a,axis=0)) #sum of columns
print(np.sum(a,axis=1)) #sum of rows    

#linespace
print(np.linspace(1,10,4))

#random number generation
import random
a=random.randint(1,10)
print(a)
random.seed(6)
for i in range(5):
    print(random.randint(1,10))

import time
random.seed(time.time())
for i in range(5):
    print(random.randint(1,10))

#random number generation using numpy
print(np.random.randint(1,10)) #random number between 1 and 10
print(np.random.randint(1,10,5)) #5 random numbers between 1 and 10
print(np.random.randint(1,10,(2,3))) #2x3 matrix of random numbers between 1 and 10
np.random.seed(6)
print(np.random.randint(1,10,(2,4)))
print(np.random.rand(2,3))
print(np.random.randn(2,3)) #random numbers from standard normal distribution
print(np.random.choice([1,2,3,4,5,6,7,8,9,10])) #randomly choose one number from the list

#sorting
a=np.array([1,2,3,4,5,6,7,8,9])
print(a)
np.random.shuffle(a)
print(a)
print(np.sort(a))
print(np.argsort(a))

#concatenation
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.concatenate((a,b)))
#usning append
print(np.append(a,b))

#split
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.split(a,2)) #split into 2 equal parts
print(np.split(a,[2,5,7])) #split at index 2,5,7

#scipy
#eigan values and eigan vectors
from scipy import linalg
a=np.array([[1,2],
            [3,4]])
print(a)
x,y=linalg.eig(a)
print(f"eigan values{list(x)}, and eigan vector is {list(y)}") #eigan values and eigan vectors

#Scipy Sparse Matrix
from scipy import sparse
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a)
b=sparse.csr_matrix(a)
print(b)

# #scipy.io
# from scipy import io as sio
# a=np.ones((3,3))
# print(a)
# sio.savemat("file.mat",{"a":a}) #save the matrix in file.mat
# data=sio.loadmat("file.mat",struct_as_record=True) #load the matrix from file.mat
# print(data["a"])
