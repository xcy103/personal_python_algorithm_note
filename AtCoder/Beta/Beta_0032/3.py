import sys
from itertools import accumulate
from bisect import bisect_left
n,q = list(map(int,sys.stdin.readline().split()))
m = []
for _ in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))
que = []
for _ in range(q):
    que.append(int(sys.stdin.readline().strip()))
m.sort()

pre = [0]*(n+1)
for i in range(n):
    pre[i+1] = pre[i]+m[i][1]
res = []
t = [x[0] for x in m]
for i in range(q):
    idx = bisect_left(t,que[i])
    res.append(str(pre[-1]-pre[idx]))
print('\n'.join(res))

