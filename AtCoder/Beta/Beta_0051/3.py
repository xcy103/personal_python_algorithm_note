import sys
max = lambda a,b: a if a>b else b
n,m,k = map(int,input().split())

c = []
p = []
for _ in range(n):
    cc,pp = map(int,input().split())
    c.append(cc)
    p.append(pp)

vis = set()
for _ in range(m):
    u,v = map(int,input().split())
    mask = 0
    mask|=1<<(u-1)
    mask|=1<<(v-1)
    vis.add(mask)

costs = {}
prof = {}
for mask in range(1<<n):
    total = 0
    g = 0
    for i in range(n):
        if mask>>i&1:
            total+=c[i]
            g+=p[i]
    costs[mask] = total
    prof[mask] = g

ans = 0
for mask in range(1<<n):
    total = 0
    if costs[mask]>k:continue
    ret = False
    for f in vis:
        if (f&mask)==f:
            ret = True
            break
    if ret:continue
    ans = max(ans,prof[mask])
print(ans)
