#creating module
def changes(a):
    a.append(4)
    return a
if __name__=="__main__":
    s=[1,2,3]
    print(changes(s))