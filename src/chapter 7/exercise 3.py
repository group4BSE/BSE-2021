try:
    name=input("Enter file name:")
    count=0
    if name=="na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        file=open(fr"C:\Users\Frank\Desktop\GROUP-4\BSE-2021\src\files\{name}","r")
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                count+=1
        print(f"There were {count} subject lines in {name}")
except:
    print(f"File cannot be opened: {name}")