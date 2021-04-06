hours=input("enter the number of hours worked")
hourly_rate=input("enter the rate per hour")

#to check if hours worked are numeric
try:
    hrs=float(hours)
    rate2=float(hourly_rate)

    gross_pay= hrs * rate2
    print("pay is:", gross_pay)
    #if input is numeric, the gross pay is calcultaed

#if input is not numeric, an error is printed
except:
    print("error, please enter numeric input")

