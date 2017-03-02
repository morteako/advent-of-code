import hashlib
import collections
import functools
salt = "zpqevtbw"
# salt = "abc"

m = hashlib.md5

def inRow3(str):
    for i,c in enumerate(str):
        if str[i:].startswith(c*3):
            return c
        # dict[c] = 0
    return ""

@functools.lru_cache(maxsize=None)
def hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

@functools.lru_cache(maxsize=None)
def hash2017(s,i=2017):
    for _ in range(i):
        s = hash(s)
    return s

triples = []
# print(hash2017("abc0"))
# xxx
for i in range(10000000000000000000):
# for i in [89]:
    if len(triples) >= 64:
        break
    # d = (salt+str(i)).encode('utf-8')
    # res = hash2017(salt+str(i),1)
    res = hash2017(salt+str(i))
    # res = hashlib.md5((salt+str(i)).encode("utf-8"))
    print(i)
    c = inRow3(res)
    if not c:
        continue
    for n in range(i+1,i+1001):
        # h = (salt+str(n)).encode('utf-8')
        # res2 = m(h).hexdigest()
        res2 = hash2017(salt+str(n))
        if c*5 in res2:
            # print("<{}>".format(c))
            triples += [i]
            print(triples)
            # print(res2)
            break
            
print("hei")
print(triples[63:],len(triples))