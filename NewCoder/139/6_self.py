import sys
from collections import deque

mod = 998244353
n = int(sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
ind = [0]*(n+1)
vis = [False]*(n+1)
g = [0]*(n+1)
for i,x in enumerate(arr):
    g[i+1] = x
    ind[x]+=1

res = 1
q = deque()
for i in range(1,n+1):
    if ind[i]==0:
        q.append(i)
t = 0
while q:
    cur = q.popleft()
    vis[cur] = True
    t+=1
    nxt = g[cur]
    ind[nxt]-=1
    if ind[nxt]==0:
        q.append(nxt)
res = pow(25,t,mod)

for i in range(1,n+1):
    if not vis[i]:
        curr = i
        L = 0
        while not vis[curr]:
            vis[curr] = True
            curr = g[curr]
            L += 1
        term1 = pow(25, L, mod)
        if L % 2 == 0:
            ring_ways = (term1 + 25) % mod
        else:
            ring_ways = (term1 - 25 + mod) % mod
        
        ans = (ans * ring_ways) % mod