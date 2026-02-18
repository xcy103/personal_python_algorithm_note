MAXN = 200001

n = 0
g = [[] for _ in range(MAXN)]

start = 0
end = 0
dist = [0] * MAXN
last = [0] * MAXN

d = 0
dp = [False]*MAXN
com = 0
def add_edge(u, v, w):
    g[u].append([v, w])
    g[v].append([u, w])

def dfs(u,f,c):
    global last,dist,g
    last[u] = f
    dist[u] = c
    for v, w in g[u]:
        if v != f:
            dfs(v, u, c + w)

def road():
    global start, end, d

    dist[1] = 0
    dfs(1, 0, 0)
    start = 1
    for i in range(2, n + 1):
        if dist[i] > dist[start]:
            start = i
    
    
    dfs(start, 0, 0)
    end = 1
    for i in range(1, n + 1):
        if dist[i] > dist[end]:
            end = i
    d = dist[end]

def maxDistanceExceptDiameter(u, f, c):
    ans = c
    for v, w in g[u]:
        if v != f:
            ans = max(ans, maxDistanceExceptDiameter(v, u, c + w))
    return ans

def solve():
    global com

    road()
    x = end
    while x != 0:
        dp[x] = True
        x = last[x]
    
    l = start
    r = end

    i = last[end]
    while i != start:
        maxDist = maxDistanceExceptDiameter(i, 0, 0)
        if maxDist == d - dist[i]:
            r = i
        if maxDist == dist[i] and l==start:
            l = i
        
        i = last[i]

    if l==r:
        com = 0
    else:
        com = 1
        i = last[r]
        while i != l:
            com += 1
            i = last[i]