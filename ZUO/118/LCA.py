# LIMIT = 20
# g = []
# deep = []
# up = []
# power = []

# def log2(n):
#     return (n&-n).bit_length()-1

# def build(n):
#     global g,deep,up,power
#     power = log2(n)
#     g = [[] for _ in range(n+1)]
#     deep = [0] * (n+1)
#     up = [[0] * (power+1) for _ in range(n+1)]

# def add_edge(u,v):
#     g[u].append(v)
#     g[v].append(u)

# def dfs(u,f):
#     deep[u] = deep[f]+1
#     up[u][0] = f

#     for p in range(1,power+1):
#         up[u][p] = up[up[u][p-1]][p-1]
    
#     for v in g[u]:
#         if v!=f:
#             dfs(v,u)

# def lca(a,b):
#     if deep[a]<deep[b]:
#         a,b = b,a
#     for p in range(power,-1,-1):
#         if deep[up[a][p]]>=deep[b]:
#             a = up[a][p]

#     if a==b:
#         return a
#     #这个函数在最后一步结束，再跳一次就是LCA了
#     for p in range(power,-1,-1):
#         if up[a][p]!=up[b][p]:
#             a = up[a][p]
#             b = up[b][p]
#     return up[a][0]

import sys

def get_lca_result(n,m,root,edges,queries):
    g = [[] for _ in range(n+1)]
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)
    
    limit = 17
    deep = [0] * (n+1)
    stjump = [[0] * limit for _ in range(n+1)]

    def dfs(u,f):
        deep[u] = deep[f]+1
        stjump[u][0] = f

        for p in range(1,limit):
            stjump[u][p] = stjump[stjump[u][p-1]][p-1]
            if stjump[u][p]==0: break

        for v in g[u]:
            if v!=f:
                dfs(v,u)
    
    dfs(root,0)

    results = []

    for a,b in queries:
        if deep[a]<deep[b]:
            a,b = b,a
        for p in range(limit-1,-1,-1):
            if deep[stjump[a][p]]>=deep[b]:
                a = stjump[a][p]
        if a==b:
            results.append(a)
        
        for p in range(limit-1,-1,-1):
            if stjump[a][p]!=stjump[b][p]:
                a = stjump[a][p]
                b = stjump[b][p]
        results.append(stjump[a][0])
    
    return results
        

