fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.strip()
    line = line.split()
    
    for words in line:
        if words not in lst: #comparing words
            lst.append(words)
        else: continue
lst.sort()
print lst

''' As it is going through it's loop and finds the words,
it goes through a new loop and checks if any of the words are
in my lst file. If they are not in the lst file, then it adds
them. After that simply sort and print the words! '''
