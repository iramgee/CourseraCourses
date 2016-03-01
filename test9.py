# make sure file exists
try:
    name = raw_input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    fh = open(name)
except:
    print 'File cannot be opened: '


# when file works we move forward create dictionary
cts = dict()

# for a new variable in a variable from above
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ')  : continue
    words = line.split()
    words = words[1]
# this will get all the emails and add a count to them if they already exist in dict
    cts[words] = cts.get(words,0) + 1

bc = None
bw = None

for word,count in cts.items():
    if bc is None or count > bc:
        bw = word
        bc = count

print bw, bc
    
