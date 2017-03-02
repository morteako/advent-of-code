

import numpy as np

num = 9
num = 3005290
# num = 3005290

elves = [x+1 for x in range(num)]

length = num


i = 0
counter = 0
while len(elves) > 1:
    if not counter % 1000:
        print(len(elves))
    counter += 1
    v = i % len(elves)
    opp = (i + len(elves)//2) % len(elves)
    # print(v,elves[v],i,opp,elves,"del",elves[opp])
    del elves[opp]
    if v == len(elves):
        i+=2
    else:
        i += 1
 
    
print(elves)
    
# print("svar:",  elves)
# print("svar:",  elves[0][1])


