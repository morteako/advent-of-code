from itertools import permutations

file = open("day3.txt","r")

lines = file.readlines()
count = 0

lines = [l.split() for l in lines]

for i in range(0,len(lines),3):
    for j in range(3):
        # print(lines[i])
        numbers = [lines[i][j],lines[i+1][j], lines[i+2][j]]
        print(numbers)
        numbers = [int(x) for x in numbers]
        numbers.sort()  
        a,b,c = numbers
        count += a+b > c

   
  
print(count)
