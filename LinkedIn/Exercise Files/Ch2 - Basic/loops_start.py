#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<5):
    print(x , end=" ")
    x+=1

  # define a for loop
  for x in range(5,10):
    print(x, end=" ")

  # use a for loop over a collection
  days=["Mon","tue","wed","thu"]
  for x in days:
    print(x,end=" ")
  
  # use the break and continue statements
  for x in range(5,10):
    #if (x==7): break
    if (x%2==0): continue
    print(x, end=" ")

  #using the enumerate() function to get index 
  days=["Mon","tue","wed","thu"]
  for i,x in enumerate(days):
    print(i, x)


if __name__ == "__main__":
  main()
