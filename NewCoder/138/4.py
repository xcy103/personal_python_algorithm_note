import sys

sys.setrecursionlimit(60000)
data = sys.stdin.read()
cases = int(data[0])
idx = 1
res = []

for _ in range(cases):
    n = data[idx]
    idx+=1
    c = [0]
    for _ in range(n):
        c.append(data[idx])
        idx+=1
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = data[idx],data[idx+1]
        idx+=2
        g[a].append(b)
    ans = 0
    def dfs(u,f,color,nums):
        global ans
        for v in g[u]:
            if v==f: continue
            if c[v]==color:
                ans+=nums
                dfs(v,u,color,nums+1)
            else:
                dfs(v,u,c[v],1)
    dfs(1,0,c[1],1)
    res.append(str(ans))

print('\n'.join(ans))