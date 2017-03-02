pr = print
nr = 1

def dragon(a):
    b = a
    brev = b[::-1]
    switched = "".join(["0" if c == "1" else "1" for c in brev])
    return a + "0" + switched
    
def checksum(s):
    pairs =  [s[i:i+2] for i in range(0, len(s), 2)]
    for p in pairs:
        sameStr += str(int(p[0] == p[1]))
    if len(sameStr) % 2:
        return sameStr
    else:
        return checksum(sameStr)

disk = "10111011111001111"
# disk = "10000"
# while len(disk) < 272:
# length = 20
length = 35651584
while len(disk) < length:
    pr(len(disk))
    disk = dragon(disk)
# pr(disk)
print(checksum(disk[:length]))

# print(checksum("110010110100"))
    