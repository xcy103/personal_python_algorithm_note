import sys

data = sys.stdin.read().split()
t = data[0]
idx = 1
res = []
for _ in range(t):
    n = data[idx]
    idx+=1
    arr = data[idx:idx+n]
    idx+=n
    if sum(arr)%n:
        res.append('No')
        continue
    c0 = 0
    c1 = 0
    for i in range(n):
        if i%2==0:
            c0+=arr[i]
        else:
            c1+=arr[i]
    l0 = (n+1)//2
    l1 = n//2
    if c0%l0==0 and c1%l1==0 and c0//l0==c1//l1:
        res.append('Yes')
    else:
        res.append('No')
print('\n'.join(res))


