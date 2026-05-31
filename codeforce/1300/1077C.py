import sys
from collections import Counter
n = int(input())
arr = list(map(int,input().split()))
c = Counter(arr)
s = sum(arr)
res = []
mp = set(arr)
for i,x in enumerate(arr):
    s-=x
    if c[x]==1:
        mp.remove(x)
    if s%2==0 and s//2 in mp:
        res.append(i+1)
    if c[x]==1:
        mp.add(x)
    s+=x
if not res:
    print(0)
else:
    print(len(res))
    print(*res)
        