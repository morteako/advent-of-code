file = open("day12.txt","r")

lines = file.read().split("\n")

class Reg:
    def __init__(self):
        self.v = 0
    
    def inc(self):
        self.v += 1
        
    def dec(self):
        self.v -= 1
        
    def notZero(self):
        return self.v != 0

regs = {}
for c in "abcd":
    regs[c] = Reg()

regs["c"].v = 1
for i in regs:
    print(regs[i].v)

    
i = 0
try:
    while True:
        line = lines[i].split()
        if line[0] == "inc":
            regs[line[1]].inc()
        elif line[0] == "dec":
            regs[line[1]].dec()
        elif line[0] == "cpy":
            x,y = line[1],line[2]
            if x in "abcd":
                regs[y].v = regs[x].v
            else:
                regs[y].v = int(x)
        elif line[0] == "jnz":
            x,y = line[1],line[2]
            if x in "abcd":
                x = regs[x].v
            if x != 0:
                i += int(y) - 1
                
        i += 1
except IndexError:
    print(regs["a"].v)