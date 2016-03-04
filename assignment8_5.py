fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
'''
for line in fh:
    line = line.rstrip()
    words = line.split()
    if words == [] : continue
    if words[0] != 'From'  : continue
    count = count + 1
    words = words[1]
    print words

print "There were", count, "lines in the file with From as the first word"

'''
lst = []
for line in fh:
    line = line.strip()

    if line == '' : continue
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From': continue
    lst.append(words[1])
    print words[1]
print  "There were", len(lst), "lines in the file with From as the first word"
