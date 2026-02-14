import sys
from collections import Counter
from math import sqrt
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip()))

sum_arr = sum(arr)
max_arr = max(arr)

c = Counter(arr)
d = []

uni = sorted(c.keys())

for i in range(max_arr,int(sqrt(sum_arr))+1):
    if sum_arr%i==0:
        uni.append(i)

def check(l):
    cc = c.copy()
    for v in uni:
        freq = cc[v]
        if freq==0:
            continue
        if v==l:
            cc[v] = 0
            continue
        
        target = l - v
        if target==v:
            if freq % 2 != 0:
                return False
            cc[v] = 0
        else:
            if cc[target]<freq:
                return False
            cc[target]-=freq
            cc[target] = 0
    return True

ans =[]

for L in d:
    if check(L):
        ans.append(str(L))

sys.stdout.write(" ".join(ans) + "\n")

