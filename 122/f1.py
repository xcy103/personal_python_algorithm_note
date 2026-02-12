# 这个没啥说的，书上差分标准模板
def max_point_weight(n,edges,queries):
    """
    n       : 节点数，1 ~ n
    edges   : [(u, v), ...]  树的边
    queries : [(a, b), ...]  路径加一操作
    return  : 最大点权
    """

    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    LOG = n.bit_length()-1
    stjump  = [[0] * (LOG + 1) for _ in range(n + 1)]
    num = [0] * (n + 1)
    deep = [0] * (n + 1)

    def dfs1(u,f):
        deep[u] = deep[f] + 1
        stjump[u][0] = f
        for p in range(1,LOG + 1):
            stjump[u][p] = stjump[stjump[u][p-1]][p-1]

        for v in g[u]:
            if v == f:
                continue
            dfs1(v,u)
    
    def lca(u,v):
        if deep[u] < deep[v]:
            u,v = v,u
        
        for p in range(LOG,-1,-1):
            if deep[stjump[u][p]] >= deep[v]:
                u = stjump[u][p]
        
        if u == v:
            return u
        
        for p in range(LOG,-1,-1):
            if stjump[u][p] != stjump[v][p]:
                u = stjump[u][p]
                v = stjump[v][p]
        
        return stjump[u][0]
    
    def dfs2(u,f):
        for v in g[u]:
            if v == f:
                continue
            dfs2(v,u)
       
        for v in g[u]:
            if v == f:
                continue
            num[u] += num[v]
    
    dfs1(1,0)

    for u,v in edges:
        c = lca(u,v)
        num[u] += 1
        num[v] += 1
        num[c] -= 1
        if stjump[c][0] != 0:
            num[stjump[c][0]] -= 1
        
    dfs2(1,0)

    return max(num[1:])