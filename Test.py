myfile=open("fileone.txt","r")
str=myfile.readline(6)
str=myfile.readline()
str=myfile.readline(8)
print(str)
myfile.close()


#String Magic method
class MyString:
    def __str__(self):
        return 'My String !'
Out=str(MyString())
print(Out) #My String !

