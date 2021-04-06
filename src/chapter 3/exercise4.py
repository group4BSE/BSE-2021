age= input("enter your age")

try:
    voter_age = int(age)
    if voter_age >=18:
        print("you can vote")
    elif 0< voter_age<=17:
        print("too young to vote")
    elif voter_age<0:
        print("you are a time traveller")
except:
    print("error, please enter numeric input")
