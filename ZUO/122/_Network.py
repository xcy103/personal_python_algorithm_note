import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 读入
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

LIMIT = 17
deep = [0] * (n + 1)
stjump = [[0] * LIMIT for _ in range(n + 1)]
def dfs1(u,f):
    deep[u] = deep[f] + 1
    stjump[u][0] = f
    for p in range(1,LIMIT):
        stjump[u][p] = stjump[stjump[u][p-1]][p-1]
    for v in g[u]:
        if v!=f:
            dfs1(v,u)

def lca(a,b):
    if deep[a]<deep[b]:
        a,b = b,a
    
    for p in range(LIMIT-1,-1,-1):
        if deep[stjump[a][p]]>=deep[b]:
            a = stjump[a][p]
    if a==b:
        return a
    for p in range(LIMIT-1,-1,-1):
        if stjump[a][p]!=stjump[b][p]:
            a = stjump[a][p]
            b = stjump[b][p]
    return stjump[a][0]

dfs1(1,0)
num = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    L = lca(u, v)
    num[u] += 1
    num[v] += 1
    num[L] -= 2

ans = 0
def dfs2(u,f):
    global ans
    for v in g[u]:
        if v!=f:
            dfs2(v,u)
    
    for v in g[u]:
        if v!=f:
            w = num[v]
            if w==0:
                ans+=m
            elif w==1:
                ans+=1
            num[u]+=num[v]
dfs2(1,0)
print(ans)