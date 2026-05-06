import sys


t = int(input())

res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = [0]+arr+[0]
    f = 1
    for i in range(1,n+1):
        if arr[i]>max(arr[i-1],arr[i+1]):
            res.append('No')
            f = 0
            break
    if f:
        res.append('Yes')

print('\n'.join(res))
