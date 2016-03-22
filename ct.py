#! python2.7
import requests
import webbrowser
from ct_vars import *
from selenium import webdriver
import time

today = (time.strftime("%m/%d/%Y"))
month = time.strftime('%m')
if month == 1:
    month = 'Jan'
if month == 2:
    month = 'Feb'
if month == 3:
    month = 'Mar'
if month == 4:
    month = 'Apr'
if month == 5:
    month = 'May'
if month == 6:
    month = 'Jun'
if month == 7:
    month = 'Jul'
if month == 8:
    month = 'Aug'
if month == 9:
    month = 'Sep'
if month == 10:
    month = 'Oct'
if month == 11:
    month = 'Nov'
if month == 12:
    month = 'Dec'

day = time.strftime('%d')
year = time.strftime('%y')


print 'Today\'s date is', today
inp = raw_input("What day would you like the file run from? \n use this format: Jan 1 ,2016 ")
inp = inp.capitalize()
fday = inp[3]

print 'Let\'s get a report starting on ',inp,'and ending',today,'!'

browser = webdriver.Firefox()
type(browser)
browser.get(ct_website)
# webbrowser.open('https://cp.socketlabs.com/login?ReturnUrl=%2f')
# webbrowser.open('https://cp.socketlabs.com/account')
# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try:
    unElem = browser.find_element_by_name(un_elem_name)
    unElem.send_keys(ct_username)
    pwElem = browser.find_element_by_name(ct_pw_elem)
    pwElem.send_keys(ct_pw)
    loginClick = browser.find_element_by_name('thirdColumn:login:_id9:_id14')
    loginClick.click() # logs us in after everything has been filled

except:
    print 'Was not able to find an element with that name!' , unElem
    quit()

# click on the total messages sent link
try:
    sentMessages = browser.find_element_by_link_text('Total Messages Sent')
    sentMessages.click()
except:
    print 'Not able to do this'
    quit()

# change the date range of sent messages

# open from date calendar and specify the from date
try:
    fpopCal = browser.find_element_by_text('body:viewReportSentCampaign:viewReportData:fromDatePopupButton')
    fpopCal.click()
except:
    print 'Could not open "FROM" calendar'
    webbrowser.close()
    quit()

# specify the from date
try:
    fromDate = browser.find_element_by_name(fday)
    fromDate.click()
    
except:
    print 'Could not validate "FROM" date'
    webbrowser.close()
    quit()

# To date is defaulted to today's date

# once dates are changed, auto submit
try:
    dateSubmit = browser.find_element_by_name('body:viewReportSentCampaign:viewReportData:toDateInputDate')
    dateSubmit.click()

except:
    print 'Couldn\'t submit'
    webbrowser.close()
    quit()
