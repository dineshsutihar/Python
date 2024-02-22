#Challenge program for file handling files with directories
 
import os

totalbytes = 0

dirlist=os.listdir()
for entry in dirlist:
    if os.path.isdir(entry):
        filesize=os.path.getsize(entry)
        totalbytes += filesize

os.makedirs("result")

resultfile=open("result/result.txt","w")
if resultfile.mode=="w":
    resultfile.write("Total bytes in directorie: " + str(totalbytes)+ "\n")
    resultfile.write("Files in directory: \n")
    resultfile.write("------------------- \n")
    for entry in dirlist:
        if os.path.isfile(entry):
            resultfile.write(entry + "\n")
            
    resultfile.close()

