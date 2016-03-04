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
    time = words[5].split(':')
    time = time[0]
#    print time
    cts[time] = cts.get(time,0)+1
# this will get all the times and add a count to them if they already exist in dict

lst = []

for key, val in cts.items():
    lst.append( (key, val) )

lst.sort()

for key, val in lst[:] :
    print key, val



'''
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages. You can pull
the hour out from the 'From ' line by finding the time and then splitting
the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''

'''
final output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
