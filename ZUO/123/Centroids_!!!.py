import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())

g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

size = [0] * (n + 1)
maxsub = [0] * (n + 1)
inner1 = [0] * (n + 1)
inner2 = [0] * (n + 1)
choose = [0] * (n + 1)

outer = [0] * (n + 1)

def dfs1(u,f):
    size[u] = 1
    for v in g[u]:
        if v==f:continue
        dfs1(v,u)

        size[u]+=size[v]
        if size[v]>size[maxsub[u]]:
            maxsub[u] = v
        
        if size[v]<=n//2:
            inner_size = size[v]
        else:
            inner_size = inner1[v]
        
        if inner_size>inner1[u]:
            choose[u] = v
            inner2[u] = inner1[u]
            inner1[u] = inner_size
        elif inner_size>inner2[u]:
            inner2[u] = inner_size
    
def dfs2(u,f):
    for v in g[u]:
        if v==f:continue

        if n-size[v]<=n//2:
            outer[v] = n-size[v]
        else:
            if choose[u]!=v:
                outer[v] = max(outer[u],inner1[u])
            else:
                outer[v] = max(outer[u],inner2[v])

        dfs2(v,u)
    

def check(u):
    if size[maxsub[u]]>n//2:
        return size[maxsub[u]] - inner1[maxsub[u]]<=n//2
    
    if n-size[u]>n//2:
        return n-size[u]-outer[u]<=n//2

    return True

dfs1(1, 0)
dfs2(1, 0)

ans = []
for i in range(1, n + 1):
    ans.append("1" if check(i) else "0")

print(" ".join(ans))