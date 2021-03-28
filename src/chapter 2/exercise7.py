amount = float(input("Enter amount: "))

if amount > 20:
    ere = int(amount//20)
    amt = ere*20
    print(str(ere) + " twenties")

    rem1 = int((amount % 20))

    tet = rem1//10
    amt2 = tet*10
    print(str(tet) + ' tens')

    rem2 = (rem1 % 10)

    ket = rem2//5
    amt3 = ket*5
    print(str(ket) + " fives")

    rem3 = rem2 % 5

    mtt = rem3 // 1
    amt4 = mtt*1
    print(str(mtt) + " Ones")

    dec = amount-(amt + amt2 + amt3 + amt4)

    tm = dec//0.25
    print(str(int(tm))+' Quarters')

    tk = dec % 0.25
    print(str(int(tk//0.1)) + ' Dimes')

    sr = tk % 0.1
    print(str(int(sr//0.05)) + ' Nickels')

    p = sr % 0.05
    print(str(int(p // 0.01)) + ' Pennies')

