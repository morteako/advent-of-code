import hashlib
import collections

door = "ffykfhsq"

m = hashlib.md5
password = {}
count = 0
for i in range(10000000000000000000000000):
    d = (door+str(i)).encode('utf-8')
    # print(d)
    
    res = m(d).hexdigest()
    if res.startswith("00000"):
        index = res[5]
        if index in "01234567":
            print(res,index,res[6],i)
            if int(index) in password:
                continue
            print(index in password, index, password.keys())
            password[int(index)] = res[6]
            if len(password) == 8:
                print("break") 
                break
print(password)
print("".join([password[x] for x in range(8)]))



