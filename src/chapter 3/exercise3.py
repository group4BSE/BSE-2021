score_x=input("enter the score")

try:
    score = float(score_x)
    #(check if score is numeric)
    if 0 < score < 1.0:
        if score >= 0.9:
            print(score, "A")
        elif score >= 0.8:
            print(score, "B")
        elif score >= 0.7:
            print(score, "C")
        elif score >= 0.6:
            print(score, "D")
        elif score < 0.6:
            print(score, "F")
    else:
        print("error, value is out of range")
except:
    print("error, enter numeric input")
