hours=int(input("enter hours worked"))
hourly_rate=float(input("enter the rate"))
if hours>40:
    new_rate= 1.5 * hourly_rate
    gross_pay=hours * new_rate
    print("pay is:", gross_pay)
else:
     gross_pay= hours * hourly_rate
     print("pay is:", gross_pay)