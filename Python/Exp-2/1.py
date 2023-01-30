file_name = input("Enter file name: ")
fh = open(file_name)
lst = list()
for line in fh:
    line.rstrip()
    word = line.split()
    for j in word:
        lst.append(j)
print(lst)
