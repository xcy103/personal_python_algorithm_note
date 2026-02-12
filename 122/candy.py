# 相邻一对是一组查询，注意重复，最后减去即可

def squirrel_home(n,travel,edges):
    """
    n      : 节点数
    travel : 长度 n 的数组，下标从 1 开始或 0 开始都行（下面按 1 开始写）
    edges  : [(u, v), ...]  树的边
    return : num[1..n]，每个节点至少需要准备的糖果数
    """
    
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    head_query = [[] for _ in range(n + 1)]
    vis = [False] * (n + 1)
    unionfind = list(range(n + 1))
    father = [0] * (n + 1)
    ans = [0] * n
    num = [0] * (n + 1)

    def find(x):
        if unionfind[x] != x:
            unionfind[x] = find(unionfind[x])
        return unionfind[x]

    def tarjan(u,f):
        vis[u] = True
        

        for v in g[u]:
            if v == f:
                continue
            tarjan(v,u)
        
        for v,idx in head_query[u]:
            if vis[v]:
                ans[idx] = find(v)

        father[u] = f
        unionfind[u] = f
    

    def dfs(u,f):
        for v in g[u]:
            if v == f:
                continue
            dfs(v,u)
            
        for v in g[u]:
            if v == f:
                continue
            num[u] += num[v]
    
    for i in range(1,n):
        u = travel[i]
        v = travel[i+1]
        head_query[u].append((v,i))
        head_query[v].append((u,i))
    
    tarjan(1,0)

    for i in range(1,n):
        u = travel[i]
        v = travel[i + 1]
        lca = ans[i]
        lcafather = father[lca]

        num[u] += 1
        num[v] += 1
        num[lca] -= 1
        if lcafather:
            num[lcafather] -= 1
    
    dfs(1,0)

    for i in range(2,n+1):
        num[travel[i]]-=1
    
    return num[1:]