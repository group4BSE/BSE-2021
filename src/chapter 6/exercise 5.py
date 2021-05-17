string = 'X-DSPAM-Confidence:0.8475'
first=string.find(":")
find=string[first+1:]
find=float(find)
print(type(find))