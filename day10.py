file = open("day10.txt","r")

lines = file.read().split("\n")

class Bot:
    def __init__(self,vals=[]):
        self.vals = []
        self.low = -1
        self.high = -1
        
    def add(self,x):
        self.vals += [x]
        
    def min(self):
        return min(self.vals)
    
    def max(self):
        return max(self.vals)
        
    def send(self):
        if not self.vals:
            return
        if self.low != -1:
            self.low.add(min(self.vals))
        if self.high != -1:
            self.high.add(max(self.vals))
  
class Output(Bot):
    def add(self,x):
        self.vals + x


def putBot(nr,val,bs):
    if nr in bs:
        bs[nr].add(val)
    else:
        bs[nr] = Bot([val])
        
def putOutput(nr,val,outs):
    if nr in outs:
        outs[nr].add(val)
    else:
        outs[nr] = Output([val])

def getOutput(nr,outs):
    if nr in outs:
        return outs[nr]
    else:
        outs[nr] = Output()
        return outs[nr]
        
def getBot(nr,bs):
    if nr in bs:
        return bs[nr]
    else:
        bs[nr] = Bot()
        return bs[nr]
        
outputs = {}
bots = {}

for line in lines:
    s = line.split()
    if line.startswith("value"):
        val = int(s[1])
        putBot(s[4],val,bots)
    else:
        b = getBot(s[1],bots)
        if s[5] == "bot":
            l = getBot(s[6],bots)
        else:
            l = getOutput(s[6],outputs)
        b.low = l
        if s[-2] == "bot":
            h = getBot(s[-1],bots)
        else:
            h = getOutput(s[-1],outputs)
        b.high = h
            
for bo in bots:
    bots[bo].send()

for o in outputs:
    print(o,outputs[o].vals)