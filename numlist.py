largest = None
smallest  = None
while True:
    inp = input("Enter a number: ")
    try:
        if inp == "done" : break
        if len(inp)< 1 : break # check for empty line

        # do the work here
        num = float(inp)
    except: print ("Invalid Input")
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
print ("Maximum is",largest)
print ("Minimum is", smallest)
