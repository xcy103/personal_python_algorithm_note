import sys
sys.setrecursionlimit(1000000)
data = 
t = int(data[0])
idx = 1
ret = []
for _ in range(t):
    n = int(data[idx])
    idx+=1
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = int(data[idx]),int(data[idx+1])
        idx+=2
        g[u].append(v)
        g[v].append(u)
    #树形DP吧
    res = [0]*(n+1)
    def dfs(u,f):
        global res
        if u!=1 and len(g[u])==1:
            return False,0
        tag = True
        d = 0
        for v in g[u]:
            if v==f:continue
            ltag,ld = dfs(v,u)
            tag&=ltag
            d+=ld
        if tag:
            res[u] = d
            return False,d
        else:
            res[u] = d+1
            return True,d+1
    dfs(1,0)
    ret.append(res[1:])

for x in ret:
    print(*x[1:])

    
