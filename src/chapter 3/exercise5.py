guests= input("enter number of expected guests")
try:
    guests_num= int(guests)
    if guests_num <= 50:
        print("it will cost $4000")
    else:
        if guests_num <=100:
            print("it will cost $10000")
        else:
            if guests_num <= 200:
                print("it will cost $15000")
            else:
                if guests_num > 200:
                    print("it will cost $20000")

except:
    print("error, enter numeric input")