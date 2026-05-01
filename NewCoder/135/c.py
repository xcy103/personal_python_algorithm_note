import sys

t = int(input())

res = []

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if n>=4 or n==1:
        res.append('YES')
    else:
        if n==2:
            res.append('YES' if arr[0]==1 and arr[1]==2 else 'NO')
        else:
            arr[0],arr[2] = min(arr[0],arr[2] ),max(arr[0],arr[2])
            res.append('YES' if arr == [1,2,3] else 'NO')

print('\n'.join(res))