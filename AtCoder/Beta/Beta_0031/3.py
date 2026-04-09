import sys
from heapq import heappush,heappop

n,d,s,t = list(map(int,sys.stdin.readline().split()))
inf = 10**18
s-=1
t-=1
g = [[] for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(i+1,n):
        if i==j:continue
        x1,y1 = arr[i][0],arr[i][1]
        x2,y2 = arr[j][0],arr[j][1]
        if (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)<=d*d:
            g[j].append(i)
            g[i].append(j)
    
dist = [inf]*n
dist[s] = 0
h = []
heappush(h,(0,s))
while h:
    k,u = heappop(h)
    if dist[u]<k:continue
    for v in g[u]:
        if dist[v]>k+1:
            dist[v] = k+1
            heappush(h,(k+1,v))
print(-1 if dist[t]==inf else dist[t])
