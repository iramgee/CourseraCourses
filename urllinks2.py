import urllib
from BeautifulSoup import *


def get_url_string():
    count = 0
    url = raw_input('Enter - ')
    while count < 7:
        print 'Successfully retrieved: ',url, '\n\n'
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)

        # Retrieve all of the anchor tags
        tags = soup('a')

        lst = list()
        count = count + 1
        for tag in tags:
            name = tag.get('href', None)
            lst.append(name)
    #    print count
        url = lst[17] # grabbing url in 18th position
        print 'Retrieving: ',url
    print 'Successfully retrieved ',url 

get_url_string()
