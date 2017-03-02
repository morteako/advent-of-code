import re

file = open("day9.txt","r")

lines = file.read().split("\n")

count = 0
for line in lines:
    s = ""
    i = 0
    while i < len(line):
        print("s",s)
        print(line[i:])
        m = (re.match(r"\((\d+)x(\d+)\)",line[i:]))
        if m:
            # print("0",m.group(0))
            # print("xx",m.group(1))
            # print("xx",m.group(2))
            numChars,times = int(m.group(1)),int(m.group(2))
            i += len(m.group(0))
            
            rep = line[i:i+numChars] * times
            # print("rep",line[i:i+numChars])
            # print("rep",rep)
            s += rep
            i += numChars
        else:
            s += line[i]
            i += 1
        
            
            
        # else:
            # s += c
            # i += 1
    # print("decomp",s)
    count += len(s)
print(count)