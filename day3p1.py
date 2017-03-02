from itertools import permutations

file = open("day3.txt","r")

lines = file.readlines()
count = 0

for line in lines:
    numbers = [int(x) for x in line.split()]
    numbers.sort()  
    a,b,c = numbers
    count += a+b > c
  
print(count)
