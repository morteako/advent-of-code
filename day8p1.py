import copy
file = open("day8.txt","r")


on = "#"
off = "."

screen = []
w = 50
t = 6
for i in range(t):
    screen.append([])
    for j in range(w):
        screen[i].append(off)

def ps():
    # for i in screen[::-1]:
        # print(i)
    
    for i in screen:
        print(i)
    print("end")
    
def rotateRow(y,n):
    # n = w - n
    for i in range(n):
        screen[y] = [screen[y][-1]] + screen[y][:-1]

def rotateColumn(x,n):
    # n =
    column = [row[x] for row in screen]
    # print("hei",column)
    for i in range(n):
        column = [column[-1]] + column[:-1]
    # column = column[n-1:] + column[:n-1]
    # print("shifted",column)
    for i in range(len(column)):
        # print(i, screen[i],column[i])
        screen[i][x] = column[i]
# ps()

def setRect(x,y):

    for i in range(y):
        screen[i][:x] = on*x
        


for line in file.read().split("\n"):
    ps()
    splitted = line.split()
    if len(splitted) == 2:
        x,y = splitted[1].split("x")
        setRect(int(x),int(y))
        # setRect(int(x),int(y))
        continue
    
    val = int(splitted[2].split("=")[1])
    byVal = int(splitted[-1])
    print(val,byVal)
    if splitted[1] == "row":
        rotateRow(val,byVal)
    elif splitted[1] == "column":
        rotateColumn(val,byVal)
    
res = 0
for i in screen:
    res += i.count(on)

for i in screen:
    print("".join(i))
print(res)
    
    