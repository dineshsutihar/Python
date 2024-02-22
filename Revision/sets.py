#Create an empty set 
s = set()

#Add elements to set

s.add(2)
s.add(3)
s.add(5)
s.add(3) # it is not going to get appended to s 



print(s) 

s.remove(3)


print(f"The set has {len(s)} elements.")
