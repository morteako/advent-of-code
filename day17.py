import hashlib

def doors(path):
    puz = "lpvhkcbi"
    hash = hashlib.md5((puz+"".join(path)).encode("utf-8")).hexdigest()
    return [c in "bcdef" for c in hash[:4]]


def addTuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

def inside(tup):
    x,y = tup
    return (0 <= x <= 3) and (0 <= y <= 3)
    
res = []
dirs = [(0,1),(0,-1),(-1,0),(1,0)]
letters = "UDLR"

def walk(coord,path):
    if coord == (3,0):
        res.append(path)
        return
    doorBools = doors(path)
    for i,d in enumerate(doorBools):
        if d:
            next = addTuple(coord,dirs[i])
            if inside(next):
                walk(next,path+letters[i])
        
walk((0,3),"")

print(min(res, key=len))        #part1
print(len(max(res, key=len)))   #part2


