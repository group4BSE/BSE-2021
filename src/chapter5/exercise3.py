# GROUP 4

#TURYAHABWE MYERS
#KEITA RHENE DIDAS
#NAMAGEMBE SHADIAH


nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
print(nickel, "nickels")
print(dime, "dimes")
print(quarter, "quarters")
print(one, "ones")
print(five, "fives")
# prompt the user to enter price for item
while True:
    price = input("Enter the purchase price (xx.xx) or 'q' to quit:")
    if price == "q":
        quit()
    else:
        #checking the input value to see if its the required input

        price = float(price)
        amount = price * 100

        # for multiple remainder
        remainder = amount % 5
        if remainder == 0 and price > 0:
            print("Menu for deposits:\n")
            print(" 'a' - deposit a nickel " )
            print(" 'd' - deposit a dime ")
            print(" 'q' - deposit a quarter ")
            print(" 'o' - deposit a one dollar bill ")
            print(" 'f' - deposit a five dollar bill ")
            print(" 'c' - cancel the purchase ")

            dollars = amount // 100

            #to get the remainder in cents
            cent_s = amount % 100
            print('Amount due:', dollars, ' dollars and ', cent_s, ' cents')
            payment = 0

            #to pronpt user enter selection of their choice
            while True:
                deposit = input('Indicate your selection:')
                if deposit == 'n':
                    while True:
                        payment = payment + 5
                        amount_due = amount - payment
                        break
                    if payment < amount:
                        print(amount_due // 100, 'dollars and', amount_due % 100, 'cents')
                        continue
                    else:
                        print('please, Take your change')
                        break
                if deposit == 'd':
                    while True:
                        payment = payment + 10
                        amount_due = amount - payment
                        break
                    if payment < amount:
                        print(amount_due // 100, 'dollars and', amount_due % 100, 'cents')
                        continue
                    else:
                        break
                if deposit == 'q':
                    while True:
                        payment = payment + 25
                        amount_due = amount - payment
                        break
                    if payment < amount:
                        print(amount_due // 100, 'dollars and', amount_due % 100, 'cents')
                        continue
                    else:
                        print('please, Take your change')
                if deposit == 'o':
                    while True:
                        payment = payment + 100
                        amount_due = amount - payment
                        break
                    if payment < amount:
                        print(amount_due // 100, 'dollars and', amount_due % 100, 'cents')
                        continue
                    else:
                        print('please, take your change')
                        break
                if deposit == 'f':
                    while True:
                        payment = payment + 500
                        amount_due = amount - payment
                        break
                    if payment < amount:
                        print(amount_due // 100, 'dollars and', amount_due % 100, 'cents')
                        continue
                    else:
                        print('please, take your change')
                        break
                if deposit == 'c':
                    if payment > 0:
                        print('Please take your change')
                        break
                    else:
                        break
                else:
                    print('Invalid input')
                    continue

        else:
            print('Illegal selection: Must be a non negative multiple of 5')
        continue
