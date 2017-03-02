import numpy as np
import copy
import sys
sys.setrecursionlimit(10000)
favNr = 1362
# favNr = 10

grid = np.zeros(shape=(100,100))
UNSET = -1
SPACE = 1
WALL = 0
grid[::] = UNSET

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
print(dirs)

def fix(x,y):
    val = x*x + 3*x + 2*x*y + y + y*y
    isWall = bin(val + favNr)[2:].count('1') % 2 == 0
    grid[y,x] = isWall
    return isWall
        
        
def walk(pos,steps):
    # print(pos,steps)
    posx,posy = pos
    if posx < 0 or posy < 0:
        return
    steps[pos] = 0
    g = grid[posy,posx]
    
    if g == UNSET:
        g = fix(posx,posy)
        # print(g)
        if g == SPACE:
            if pos == (31,39):
                print(len(steps),steps)
                raise ValueError(str(steps),len(steps))
                return
            for d in dirs:
                # print(d)
                if not (d in steps):
                    dx,dy = d
                    walk((posx+dx,posy+dy),copy.copy(steps))
    else:
        return
                
try:                
    walk((1,1),{})
except ValueError as e:
    print(e)
 