amount = int(input("Enter the amount to be withdrawn (in hundreds): "))

if(amount%100==0):
    amount=amount-1
    num_100s = amount // 100
    num_50s = (amount % 100) // 50
    num_10s = (((amount % 100) % 50) // 10)+1
else:
    num_100s = amount // 100
    num_50s = (amount % 100) // 50
    num_10s = ((amount % 100) % 50) // 10

# Print the results
print("No of 10s =", num_10s)
print("No of 50s =", num_50s)
print("No of 100s =", num_100s)