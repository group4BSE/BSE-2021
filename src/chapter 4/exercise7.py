def computegrade(score):
    if 0 < score < 1.0:
        if score >= 0.9:
            return ("A")
        elif score >= 0.8:
            return ("B")
        elif score >= 0.7:
            return ("C")
        elif score >= 0.6:
            return ("D")
        elif score < 0.6:
            return ("F")
    else:
        print("error, value is out of range")


try:
    score=float(input("Enter score: \n"))
    #(check if score is numeric)

except:
    print("error, enter numeric input")
    exit()

print(computegrade(score))