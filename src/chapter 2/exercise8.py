c = int(input("enter initial amount"))
r=float(input("enter rate"))
t=int(input("enter number of years"))
n=int(input("enter number of times"))

p = c*(1+(r/n))**(t*n)
print(round(p,2))