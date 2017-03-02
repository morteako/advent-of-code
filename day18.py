firstRow = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."
# firstRow = "..^^."
# firstRow = ".^^.^.^^^^"
size = len(firstRow)

def isTrap(lcr):
    bools = [i == "^" for i in lcr]
    return bools in [[True, True, False],[False, True, True],[True, False, False],[False,False,True]]

rows = [firstRow]
res = 0
for rowNr in range(1,400000):
    if rowNr % 10000 == 0:
        print(rowNr)
    prevRow = rows[-1]
    nextRow = [None] * size
    nextRow[0] = "^" if isTrap("."+prevRow[0]+prevRow[1]) else "."
    nextRow[-1] = "^" if isTrap(prevRow[-2] + prevRow[-1] + ".") else "."
    for i in range(1,size-1):
        lcr = prevRow[i-1:i+2]
        nextRow[i] = "^" if isTrap(lcr) else "."
        
    
    rows.append("".join(nextRow))

    
# print("\n".join(rows))
print(len(rows))
    
res = 0
for i in rows:
    res += i.count(".")
print(res)