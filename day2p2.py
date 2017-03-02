
nums = {}
nums[2,2] = "1"
nums[1,1] = "2"
nums[1,2] = "3"
nums[1,3] = "4"
nums[0,0] = "5"
nums[0,1] = "6"
nums[0,2] = "7"
nums[0,3] = "8"
nums[0,4] = "9"
nums[-1,1] = "A"
nums[-1,2] = "B"
nums[-1,3] = "C"
nums[-2,2] = "D"


def get(y,x):
    if (x,y) in nums:
        return nums.get((x,y))
    else:
        return None
        
lines  = open("day2.txt").read()

x,y = 0,0
code = ""
for line in lines.split('\n'):
    for c in line:
        
        if c == 'L':
            nx,ny = -1,0
        if c == 'R':
            nx,ny = 1,0
        if c == 'D':
            nx,ny = 0,-1
        if c == 'U':
            nx,ny = 0,1
            
        rx,ry = x+nx,y+ny
        if get(rx,ry):
            x,y = rx, ry
            
    # print(get(x,y),x,y)   
    code += str(get(x,y))
print(code)