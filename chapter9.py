# count words of txt file
try:
    name = raw_input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    fh = open('mbox-short.txt')
except:
    print 'File cannot be opened: ' ,fh
    exit()
text = fh.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0)+1

    if words == [] : continue
    if words[0] != 'From'  : continue
    print words
    words = words[1]


    largeNum = None
    largeCount  = None
    for word, count in counts.items():
        print word
        if largeNum == None or count < largeNum:
            largeCount = word
            largeNum = count
            print 'debug', largeCount, largeNum
    print words, largeNum
        
