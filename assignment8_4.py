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
count = 0 # ease of use
lst = list(fh)
for line in lst:
    words  = line.split() # finding all the words in this file

    print words
