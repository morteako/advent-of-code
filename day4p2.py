import re, string
from collections import Counter

lines = open("day4.txt","r").readlines()

for line in lines:
    splitted = line.split("-")
 
    name = "-".join(splitted[:-1])
    id,checksum = re.match(r"(\d+)\[(.+)\]",splitted[-1]).groups()
   
    s = ""
    alp = string.ascii_lowercase
    for c in name:
        s = s + " " if c == "-" else s + alp[(alp.index(c) + int(id)) % 26]
    
    if "north" in s:
        print(id)
