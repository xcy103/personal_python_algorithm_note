c = [0,1,1,2,1,2]
g = [[],[2],[3,4],[],[5]]
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