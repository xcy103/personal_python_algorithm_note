import sys
from collections import deque
n,m,k,t = list(map(int,sys.stdin.readline().split()))
C = list(map(int,sys.stdin.readline().split()))
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int,sys.stdin.readline().split()))
    g[u].append(v)
    g[v].append(u)

ans = k
q = deque(C)
vis = [False]*(n+1)
ind = [0]*(n+1)
for x in C:
    vis[x] = True
while q:
    for _ in range(len(q)):
        u = q.popleft()
        
        for v in g[u]:
            if not vis[v]:
                ind[v]+=1
                if ind[v]>=t:
                    q.append(v)
                    vis[v] = True
                    ans+=1
print(ans)