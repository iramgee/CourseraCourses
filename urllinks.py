import urllib
from BeautifulSoup import *

count = 0
span = list()
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()


soup = BeautifulSoup(html)

# retrieve all span tags
span = soup('span')

lst=list()

for nums in span:
    numbers = int(nums.contents[0])
    # get a count of how many different digits on on the page
    count = count + 1


    # put all the numbers on the page in a list then add
    # using the sum function
    lst.append(numbers)
print count
print sum(lst)
