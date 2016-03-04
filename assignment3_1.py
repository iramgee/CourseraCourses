# formula to calcualte hourly salary plus overtime
hrs = input("Enter hours")
h = float(hrs)
hourly = 10.5
if h <=40:
    print (h * hourly)
else:
    ot= h -40
    otpay= hourly *1.5
    print(hourly*40+(ot*otpay))
