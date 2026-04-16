import sys
from collections import deque
n,m = list(map(int,sys.stdin.readline().split()))
T = [0] + list(map(int,sys.stdin.readline().split()))

#有向图
g = [[] for _ in range(n+1)]
ind = [0]*(n+1)
for _ in range(m):
    u,v = list(map(int,sys.stdin.readline().split()))
    g[u].append(v)
    ind[v]+=1

enter = [False]*(n+1)
q = deque()
for i in range(1,n+1):
    if ind[i]>T[i]:
        q.append(i)
        enter[i] = True
res = set()
while q:
    u = q.popleft()
    res.add(u)
    for v in g[u]:
        if enter[v]:continue
        ind[v]+=1
        if ind[v]>T[v]:
            q.append(v)
            enter[v] = True
if not res:
    print(-1)
    exit(0)
res = sorted(res)
print(*res)