# def fact(n):
#     if n==1 or n==0:
#         return n
#     else:
#         return (n*fact(n-1))

# print("fact is",fact(5))

#test123.py for just testing
list=[4,5,6]
store=[[]]
for i in range(len(list)):
    store.append([list[i]])
    for j in range(i+1,len(list)):
        store.append([list[i],list[j]])
store.append(list)
print(store)
