try:
    name=input("Enter file name:")
    file=open(fr"C:\Users\Frank\Desktop\GROUP-4\BSE-2021\src\files\{name}","r")
    read=file.read()
    print(read.upper())
except:
    print("File name doesn't exist in current directory")