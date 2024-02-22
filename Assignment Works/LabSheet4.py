#Lab Sheet 4.a 
# Example input dictionary
my_dict = {"Dic1": [6, 8, 10], "Dic2": [8, 10, 12, 1], "Dic3": [10, 16, 14, 6]}

# Initialize an empty result dictionary
result_dict = {}

# Iterate over the key-value pairs in the input dictionary
for key, value in my_dict.items():
    # Check if all values in the list are even
    all_even = all(num % 2 == 0 for num in value)
    
    # Store the result in the result dictionary
    result_dict[key] = all_even

# Print the result dictionary
print(result_dict)


print("----------------------------------------------------")

#Lab Sheet 4.b
def insertionSortRecursive(arr,n):
   if n<=1:
      return
   insertionSortRecursive(arr,n-1)
   last = arr[n-1]
   j = n-2
   while (j>=0 and arr[j]>last):
      arr[j+1] = arr[j]
      j = j-1
   arr[j+1]=last

arr = [12,11,13,5,6,0,10,33]
n = len(arr)
insertionSortRecursive(arr, n)
print("Sorted array is:")
for i in range(n):
   print(arr[i],end=' ')

