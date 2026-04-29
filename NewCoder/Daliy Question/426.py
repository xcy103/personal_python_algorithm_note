import sys

t = int(sys.stdin.readline().strip())

res = []
for _ in range(t):
    n,q = list(map(int,sys.stdin.readline().split()))
    arr = list(map(int,sys.stdin.readline().split()))
    l,r = list(map(int,sys.stdin.readline().split()))
    l-=1
    r-=1
    if n==1:
        res.append(str(arr[0]))
        continue
    tmp = arr[0]+arr[1]-(arr[0]^arr[1])
    for i in range(2,n):
        tmp = tmp + arr[i] - (tmp^arr[i])
    res.append(str(tmp))
print('\n'.join(res))