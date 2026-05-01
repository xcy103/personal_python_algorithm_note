import sys

t = int(input())

res = []

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    x = (sum(arr)+n-1)//n
    low = 0
    high = 0
    for k in arr:
        if k<x:
            low+=x-k
        else:
            high+=k-x
    res.append(str(low))

print('\n'.join(res))
