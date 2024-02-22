#
#
amount = int(input("Enter the amount in hundreds: "))
if (amount%100==0):
    no_of_100s = amount // 100 -1
    amount=100
    no_of_50s = (amount % 100) // 50
    no_of_10s = (amount % 50) // 10
else:
    no_of_100s = amount // 100
    no_of_50s = (amount % 100) // 50
    no_of_10s = (amount % 50) // 10

print("No of 10s = ", no_of_10s)
print("No of 50s = ", no_of_50s)
print("No of 100s = ", no_of_100s)

#
#
def countCurrency(amount):   
    notes = [100, 50, 10]
    notesCount = {}
     
    for note in notes:
        if amount >= note:
            notesCount[note] = amount//note
            amount = amount % note
             
    print ("Currency Count ->")
    for key, val in notesCount.items():
        print(f"{key} : {val}")
 
# Driver code
amount = 400
countCurrency(amount)

#
#
amount = int(input("Enter the amount to be withdrawn (in hundreds): "))

num_100 = amount // 100
amount %= 100

num_50 = amount // 50
amount %= 50

num_10 = amount // 10

print(f"Number of notes of 100: {num_100}")
print(f"Number of notes of 50: {num_50}")
print(f"Number of notes of 10: {num_10}")

#
#
amount = int(input("Enter the amount to be withdrawn (in hundreds): "))

# Calculate the number of 100s, 50s, and 10s
num_100s = amount // 100
num_50s = (amount % 100) // 50
num_10s = ((amount % 100) % 50) // 10

# Print the results
print("No of 10s =", num_10s)
print("No of 50s =", num_50s)
print("No of 100s =", num_100s)