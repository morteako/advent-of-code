num = 5

elves = [1] * num

length = num

while True:
    i = 0
    while len(elves) > 1:
        mod = i % length
        mod1 = (i+1) % length
        if elves[mod] == 0:
            del elves[mod]
            length -= 1
            continue
        elves[mod] += elves[mod1]
        elves[mod1] = 0
        
        del elves[mod1]
        length -= 1
        i + 1
        
