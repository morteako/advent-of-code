
f = open("day1.txt","r")

grid = [[0] * 1000] * 1000

px, py = 0,0

# dirs = [[,1],[0,1],[-1,0],[-1,0]]
dirs = [[0,1],[1,0],[0,-1],[-1,0]]

dirp = 0

visited = [(0,0)]

for s in f.read().replace(" ","").split(','):
    # print(s)
# for s in "R2, R2, R2".replace(" ", "").split(','):
# for s in "R2, L3".replace(" ", "").split(','):
# for s in "R8, R4, R4, R8".replace(" ", "").split(','):
    if s[0] == "R":
        dirp = dirp + 1 if dirp != 3 else 0
    elif s[0] == "L":
        dirp = dirp - 1 if dirp != 0 else 3
    else:
        # raise ValueError(s[0])
        print("feil")
        xxx
    
    dirx,diry = dirs[dirp]
    # px += dirx * int(s[1:])
    # py += diry * int(s[1:])
    
    for i in range(int(s[1:])):
        px += dirx
        py += diry
        
        tup = (px,py)
        if tup in visited:
            print(px,py)
            print("yu")
            print(abs(px) + abs(py))
            xxx
        else:
            visited.append(tup)
    # print(int(s[1:]))
    # print(px,py,dirx,diry)
    # print(visited)
    
    
    
print(abs(px) + abs(py))
# print(px+py)