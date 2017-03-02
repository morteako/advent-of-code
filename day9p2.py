import re

file = open("day9.txt","r")

lines = file.read().split("\n")

def decomp(str):
    s = 0
    i = 0
    while i < len(str):
        m = re.match(r"\((\d+)x(\d+)\)",str[i:])
        if m:
            numChars,times = int(m.group(1)),int(m.group(2))
            i += len(m.group(0))
            rep = decomp(str[i:i+numChars]) * times
            s += rep
            i += numChars
        else:
            s += 1
            i += 1
    return s
    
print(sum(map(decomp,lines)))
