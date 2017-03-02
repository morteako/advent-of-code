

import numpy as np

num = 5
# num = 3005290

elves = [[1,"nr"+str(x+1)] for x in range(num)]

length = num


i = 0
while len(elves) > 1:
    print(len(elves))
        
    mod = i %  len(elves)
    mod1 = (i+1) %  len(elves)
    # print(123)
    # if elves[mod][0] == 0:
    
    print(i,elves,mod,mod1,elves[mod])
        # asdasd
        # del elves[mod]
        # length -= 1
        # continue
    elves[mod][0] += elves[mod1][0]
    # print(123)
    del elves[mod1]
    # print(123)
    i += 1
    # print(i,length,elves)
    input()

print("svar:",  elves)



