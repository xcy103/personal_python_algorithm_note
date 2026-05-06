import sys
from math import gcd
t = int(input())

res = []
for _ in range(t):
    a,b = map(int,input().split())
    g = gcd(9,b)
    if b==0:
        if a==1:
            res.append([1,100])
        else:
            res.append([1,2])
    elif b==9:
        if a%2==0:
            res.append([19,99])
        else:
            res.append([91,99])
    else:
        g = gcd(9,b)
        res.append([b//g,9//g])
for arr in res:
    print(*arr)

