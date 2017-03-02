
f = open("day1.txt","r")

grid = [[0] * 1000] * 1000

px, py = 0,0

# dirs = [[,1],[0,1],[-1,0],[-1,0]]
dirs = [[0,1],[1,0],[0,-1],[-1,0]]

dirp = 0

visited = [(0,0)]

# for s in f.read().replace(" ","").split(','):
    # print(s)
# for s in "R2, R2, R2".replace(" ", "").split(','):
# for s in "R2, L3".replace(" ", "").split(','):
for s in "R8, R4, R4, R8".replace(" ", "").split(','):
    if s[0] == "R":
        dirp = dirp + 1 if dirp != 3 else 0
    elif s[0] == "L":
        dirp = dirp - 1 if dirp != 0 else 3
    else:
        # raise ValueError(s[0])
        print(s[0])
    
    dirx,diry = dirs[dirp]
    px += dirx * int(s[1:])
    py += diry * int(s[1:])
    # print(int(s[1:]))
    print(px,py,dirx,diry)
    print(visited)
    tup = (px,py)
    if tup in visited:
        print("yu")
        break
    else:
        visited.append(tup)
    
    
print(abs(0-px) + abs(0-py))
print(px+py)