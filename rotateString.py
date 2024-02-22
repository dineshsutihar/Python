strings="Python Program"
n=int(input("Enter the steps: "))
lr=input("Enter l for left and r for right:")
if (lr=="l" or "L"):
    print(strings[n::],end="")
    print(strings[:n:])
else:
    print(strings[-n::],end="")
    print(strings[:-n:])