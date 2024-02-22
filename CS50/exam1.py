#1
l1=['ABC','hello','PYthon']
print(max(l1))

#2
l2=[x+y for x in ['Hi','Fine'] for y in ['Dear', 'OK']]
print(l2)

#5
x=10
while (x<500):
    x+=200
print(x)


##4
from functools import reduce

list1=[10,12,15,7]
print(reduce(lambda x,y:x%y,list1))
print(str(reduce(lambda x,y:x+y,list1,10)))

#3
#Correct One
set1 = {2, 'PYthon', ('123', 'LMS'), False}
print(set1)

#Wrong One
set1={2,'PYthon',['123','LMS'],False}
print(set1)
