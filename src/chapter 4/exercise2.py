def investment(c,r,t,n):
    p = c * (1 + (r / n)) ** (t * n)
    return p

try:
    c = int(input("enter initial amount"))
    r=float(input("enter rate"))
    t=int(input("enter number of years"))
    n=int(input("enter number of times"))

except:
    print("invalid input!!!")
    exit()

print(f"final value is{investment(c,r,t,n):,.2f}")