import numpy as np

arr = np.array(['python', 'numpy'])
print("Original array:", arr)
print("Capitalized:", np.char.capitalize(arr))
print("Lowercase:", np.char.lower(arr))
print("Swapcase:", np.char.swapcase(arr))
print("Titlecase:", np.char.title(arr))
print("Uppercase:", np.char.upper(arr))
