import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

def f(x):
    global arr,n,k
    s = 0
    op = 0
    for i in range(n):
        s+=arr[i]
        if s>=x:
            s = 0
            op += 1
    return op>=k

l = 0
r = 2**32 - 1

while l+1<r:
    mid = (l+r)>>1
    if f(mid):l = mid
    else:
        r = mid

print(r)