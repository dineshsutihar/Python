f1=open("fileone.txt","r")
f2=open("filetwo.txt","r")
f3=open("output.txt","wt")
s1=f1.read()
f3.write(s1)
s2=f1.read()
f3.write(s2)
print(f3.tell())
f1.close()
f2.close()
f3.close()


