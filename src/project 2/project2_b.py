def open_file():
    file = input('Enter input file:')
    if file=="measles.txt":
        return file
    else:
        print("File should be \"measles.txt\"")
        exit()

def ref(i_level):
    if i_level==1:
        i_level="WB_LI"
        return i_level
    elif i_level==2:
        i_level="WB_LMI"
        return i_level
    elif i_level==3:
        i_level="WB_UMI"
        return i_level
    elif i_level==4:
        i_level="WB_HI"
        return i_level
    else:
        print("Invalid income level")

while True:
    try:
        file=open_file()
        year = int(input('Enter year:'))
        year = str(year)
        i_level = int(input('Enter income level:'))
        i_level_2=ref(i_level)
        measles = open(file, 'r')
        count=0
        add=0
        lowest=99
        highest=0
        for line in measles:
            if (i_level_2 in line[51:57]) and (year==line[88:92]):
                child=line[59:62]
                child_2=int(child)
                if child_2>highest:
                    highest=child_2
                if child_2<lowest:
                    lowest=child_2
                add+=child_2
                count+=1
        average=add/count
        print("Lowest percentage =",lowest)
        print("Highest percentage =",highest)
        print("Average percentage =",average)
        print("Success!")
        break
    except:
        print("Error!! , Invalid Input!!")
        continue
