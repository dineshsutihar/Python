#1
import numpy as np

arr = np.arange(9)
print('Orignal Shape: \n',arr)

print('3x3 order of array:\n',np.reshape(arr, (3, 3)))

#2
import numpy as np

arr = np.array([[1, 2, 3]])
print("Original array:\n",arr)
print("Transformed array:\n",np.transpose(arr))

# #3
# import math
# from scipy import constants

# print("math - pi Value =", math.pi)
# print("sciPy - pi Value =", constants.pi)


# try:
#     import numpy
#     print("Successfull")
#     import scipy
#     print("Sucessfull")
# except Exception as e:
#     print (e)
import scipy