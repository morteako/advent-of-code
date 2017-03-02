import re

file = open("day15.txt","r")

class Disc:
    def __init__(self, nr, numPos, time, pos):
        self.nr = nr
        self.numPos = numPos
        self.time = time
        self.pos = pos
    
    def move(self,n):
        # print("disc",nr,numPos,pos)
        # print(n,pos,pos+n,(pos+n)%numPos)
        return (self.pos + n) % self.numPos
        
         
    
discList = []
    
for line in file.read().split("\n"):
    splitted = line[:-1].split()
    pos = int(splitted[-1])
    nr = int(splitted[1][1:])
    time = int(splitted[6][:-1].split("=")[1])
    numPos = int(splitted[3])
    discList += [(nr,numPos,time,pos)]
    print("DDDD",discList)
    
# for i in range(1):
print(len(discList))
for i in range(1000000000000):
    discs = [Disc(a,b,c,d) for a,b,c,d in discList]
    s = 0
    for time,d in enumerate(discs):
        s += d.move(i+time+1)
        
    if s == 0:
        print("RES",i)
        break