# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
n = 0
total = 0
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.index(':')
    loc = pos +1
    dig = line[loc:]
    num = float(dig)
    for n in [num]:
        total = total + n
    linestrip = line.rstrip()

print "Average spam confidence:",total / count

# Average spam confidence: 0.750718518519
