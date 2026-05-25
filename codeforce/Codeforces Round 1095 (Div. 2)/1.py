import sys
from collections import Counter
t = int(input())

res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    op = 0
    l = 0
    while l<n:
        while l<n and arr[l]==1:
            l+=1
        if l==n:
            op+=1
            break
        op+=arr[l]
        l+=1
    res.append(str(op))
print('\n'.join(res))
