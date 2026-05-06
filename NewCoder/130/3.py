import sys


n = int(input())
g = [[] for _ in range(n+1)]

ind = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    ind[a]+=1
    ind[b]+=1

if max(ind)>3:
    print(0)
    exit(0)
else:
    s = 0
    for i in range(1,n+1):
        if ind[i]==3:
            s+=1
    print(n-s)