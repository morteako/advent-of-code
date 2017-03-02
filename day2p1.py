
x,y = 0,0

nums = [[7,8,9],[4,5,6],[1,2,3]]
   
def get(x,y):
    return nums[y+1][x+1]
    

lines  = open("day2.txt").read()

code = ""
for line in lines.split('\n'):
    for c in line:
        if c == 'L':
            x -= 1
        if c == 'R':
            x += 1
        if c == 'D':
            y -= 1
        if c == 'U':
            y += 1
            
        x = min(x,1)
        x = max(x,-1)
        y = min(y,1)
        y = max(y,-1)
        
    # print(get(x,y),x,y)   
    code += str(get(x,y))
print(code)