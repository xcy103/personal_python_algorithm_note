import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# 读入
n = int(input())
travel = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queries = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)

for i in range(1,n):
    u,v = travel[i], travel[i+1]
    queries[u].append((v,i))
    queries[v].append((u,i))

parent = list(range(n + 1))
father = [0]*(n + 1)
vis = [False]*(n + 1)

def find(x):
    while father[x]!=x:
        father[x] = father[father[x]]
        x = father[x]
    return x

def trajan(u,f):
    vis[u] = True
    father[u] = f
    for v in graph[u]:
        if v!=f:
            trajan(v,u)
            parent[v] = u
    for v,idx in queries[u]:
        if vis[v]:
            ans[idx] = find(v)
    
num = [0] * (n + 1)
def dfs(u,f):
    for v in graph[u]:
        if v!=f:
            dfs(v,u)
            num[u] += num[v]
tarjan(1, 0)

for i in range(1,n):
    u = travel[i]
    v = travel[i + 1]
    lca = ans[i]
    lf = father[lca]
 
    num[u] += 1
    num[v] += 1
    num[lca] -= 1
    if lf != 0:
        num[lf] -= 1

dfs(1, 0)   

for i in range(2, n + 1):
    num[travel[i]] -= 1

# 输出
print("\n".join(map(str, num[1:])))