total=0
count=0
while True:
    try:
        val=input("enter number")
        if val == "done":
            break
        else:
            val1=int(val)
            count=count+1
            total=total+val1
    except:
        print("invalid input")
        continue

print(total,count,total/count)