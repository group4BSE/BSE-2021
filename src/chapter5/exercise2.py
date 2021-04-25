max1=None
min1=None
while True:
    try:
        number=input("enter number")
        if number=="done":
            break
        number1=int(number)
        if (max1 and min1) is None:
            max1=number1
            min1=number1
        if number1>max1:
            max1=number1
        if number1<min1:
            min1=number1
    except:
        print("invalid input")
        continue

print(f"the maximum value is {max1}, the minimum value is{min1}")