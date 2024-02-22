def merge_files(file1, file2, output):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output, "w") as f3:
        for line in f1:
            f3.write(line)
        for line in f2:
            f3.write(line)

file1 = "fileone.txt"
file2 = "filetwo.txt"
output = "output.txt"

merge_files(file1, file2, output)

with open(output, "r") as f:
    contents = f.read()
    print(contents)
    size = f.seek(0, 2)
    print(f"The size of the output file is {size} bytes.")

    
