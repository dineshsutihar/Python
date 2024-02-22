str1="Hai"
str2="hello"
print(str1+" "+str2)

#Type List
lst=[1,10.1,"hai"]
print(type(lst))
print(lst)

#Tuple
#It is same as list stored all the elements are seperated by comma(,) enclosed by brackets 
tup=(1,10.1,"hello")
print(type(tup))
print(tup)

#set
#Unordered collection of elements each elements are unique and cannot be canged, each elements are enclosed b { }
my_set={1,3,5,7}
print(type(my_set))
print(my_set)
#example
x=set("hello")
print(x)
y=set(("AA","BB","BB","AA","C"))
print(y)

#Dictionary
# it is a container it can store ordered elements each elements having {key:value} pack and surrunded by{ }
des={101:'AAA',102:'Dinesh',103:'Umesh'}
print(type(des))
print(des)
print(des[102])

#Boolean
#Stores Trues and false
str=True
print(type(str))
str2="Python"
print(str2==str)