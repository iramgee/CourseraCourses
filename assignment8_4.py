fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.strip()
    line = line.split()
    for words in line:
        if words not in lst:
            lst.append(words)
        else: continue
lst.sort()
print lst
