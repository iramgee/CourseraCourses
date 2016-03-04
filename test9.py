# make sure file exists
try:
    name = raw_input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    fh = open(name)
except:
    print 'File cannot be opened: '


# when file works we move forward create dictionary
cts = dict()

# for a new variable in a variable from above
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[1]
# this will get all the emails and add a count to them if they
# already exist in dict
    cts[words] = cts.get(words, 0) + 1
# print cts
# we will write to these variables
bc = None
bw = None

# finding the most used words and counting them
for word, count in cts.items():
    # looping through counting the biggest reiteration and saving that word
    if bc is None or count > bc:
        bw = word
        bc = count
# print the largest iteration with it's word
print bw, bc
