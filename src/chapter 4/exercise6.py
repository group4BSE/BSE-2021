def computepay(hours,rate):
    if hours>40:
       new_rate= 1.5 * hourly_rate
       gross_pay=hours * new_rate

    else:
        gross_pay= hours * hourly_rate
    print("pay is:", gross_pay)

try:5
    hours = int(input("enter hours worked"))
    hourly_rate = float(input("enter the rate"))
except:
    print("enter numeric input")
    exit()