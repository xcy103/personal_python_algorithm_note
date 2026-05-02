
import sys

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = sum(arr)
    p0 = [0]*n
    p1 = [0]*n
    p0[-1] = 1 if arr[-1]%2==0 else 0
    p1[-1] = 1 if arr[-1]%2==1 else 0
    for i in range(n-2,-1,-1):
        p0[i] = p0[i+1]+(1 if arr[i]%2==0 else 0)
        p1[i] = p1[i+1]+(1 if arr[i]%2==1 else 0)
    op = 0
    for i in range(n-1):
        s-=arr[i]
        t = (n-1-i)*arr[i]+s
        k = 0
        if arr[i]%2==0:
            k = p1[i+1]
        else:
            k = p0[i+1]
        op += (t-k)//2
        
    res.append(str(op))

print('\n'.join(res))