# while True:
#    line = input('> ')
#    if line == "done":
#        break
#    print (line)
# print('Done')



largest = None
samllest = None
try:
    while True:
        num = input("Enter a number: ")
        digit = int(num)
        if digit == "done":
            break
except:
    print ("invalid Input")
