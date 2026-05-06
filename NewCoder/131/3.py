import sys

t = int(input())

res = []
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    l = 0
    r = 0
    while l<n and r<m:
        if a[l]>=b[r]:
            l+=1
            r+=1
        else:
            l+=1
    if r==m:
        res.append('YES')
    else:
        res.append('NO')

print('\n'.join(res))
