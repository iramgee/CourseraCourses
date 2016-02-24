# fh = open('romeo.txt')
# my_list = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
# lst = list()

# for line in fh:
#     lst = line.split() # finding words in this file
#     lst.sort()
# print lst

alist = ['Arise But It Juliet breaks east envious fair kill light moon soft sun the through what window yonder']
# fname = raw_input("Enter file name: ")
# fh = open(fname)
fh = open('romeo.txt')
for line in fh:
    lst = line.split() # finding all the words in this file
    lst.sort() # putting list in order
for x in alist:
    n = x.split()
    n.sort()
n.sort()
print n
