numbers=[]
while True:
    num=input("Enter a number:")
    if num=="done":
        break
    else:
        number=float(num)
        numbers.append(num)
        continue
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))