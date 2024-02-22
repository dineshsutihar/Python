import numpy as np

arr = np.ones((3, 3))
print("Original array:\n ",arr)

padded_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print("Array with border of zeros:")
print(padded_arr)
