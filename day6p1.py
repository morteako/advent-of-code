from collections import Counter

file = open("day6.txt","r")
lines = file.read().split("\n")

chars = [""] * len(lines[0])

for line in lines:
    for i,x in enumerate(line):
        chars[i] += x
    # print(chars)
    
res = ""
res2 = ""
for s in chars:       
    # print(Counter(s).most_common(1))
    x,y = Counter(s).most_common(1)[0]
    x2,y = Counter(s).most_common()[-1]
    res += x
    res2 += x2
print(res)
print(res2)