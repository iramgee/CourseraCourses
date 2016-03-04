# define function with OT pay at time and a half
def compute_pay_with_ot():
    ot = h - 40
    otpay = hourly * 1.5
    return(hourly * 40 + (ot * otpay))

# formula to calcualte hourly salary plus overtime

try:
    hrs = input("Enter hours: ")
    h = float(hrs)
    salary = input("Hourly rate: ")
    pay = float(salary)
    hourly = 10.5
    ot = h - 40
    otpay = hourly * 1.5
except:
    print('Error, please enter a numeric input')
    quit()
if h <= 40:
    print (h * hourly)
else:
    p = compute_pay_with_ot()
    print (p)
