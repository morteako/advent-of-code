import re, itertools,operator
from collections import Counter

import string


file = open("day4.txt","r")

lines = file.readlines()
# lines = ["qzmt-zixmtkozy-ivhz-343[aasd]"]

sum = 0
alp = string.ascii_lowercase

for line in lines:
    splitted = line.split("-")
 
    name = "".join(splitted[:-1])
    m = re.match(r"(\d+)\[(.+)\]",splitted[-1])
    id,checksum = m.groups()
    
    letters = ""
    counts = Counter(name).most_common()
    for key,group in itertools.groupby(counts,operator.itemgetter(1)):
        ls = [x[0] for x in group]
        letters += "".join(sorted(ls))
         
    if letters.startswith(checksum):
        sum += int(id)
print(sum)
