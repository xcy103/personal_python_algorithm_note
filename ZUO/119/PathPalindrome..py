import sys

input = sys.stdin.readline()

MAXN = 100001
LIMIT = 17
K = 2333

s = [0]*MAXN
deep = [0]*MAXN
kpow = [0]*MAXN
stjump = [0]*MAXN
stup = [[0]*LIMIT for i in range(MAXN)]
stdown = [[0]*LIMIT for i in range(MAXN)]

g = [[] for i in range(MAXN)]
power = 0

def log2(n):
    ans = 0
    while (1<<ans)<=n>>1:
        ans+=1
    return ans

def build(n):
    global power
    power = log2(n)

    kpow[0] = 1
    for i in range(1,n+1):
        kpow[i] = kpow[i-1]*K

def dfs(u,f):
    deep[u] = deep[f] + 1
    stjump[u][0] = f
    stup[u][0] = stdown[u][0] = s[f]

    for p in range(1,power+1):
        v = stjump[u][p-1]
        stjump[u][p] = stjump[v][p-1]
        stup[u][p] = (
            stup[u][p-1]*(kpow[1<<(p-1)]+
                          stup[v][p-1])
        )
        stdown[u][p] = (
            stdown[v][p - 1] * kpow[1 << (p - 1)] + stdown[u][p - 1]
        )
    for v in g[u]:
        if v!=f:
            dfs(v,u)

def lca(u,v):
    if deep[u]<deep[v]:
        u,v = v,u
    
    for p in range(power,-1,-1):
        if deep[stjump[u][p]] >= deep[v]:
            u = stjump[u][p]
    
    for p in range(power,-1,-1):
        if stjump[u][p]!=stjump[v][p]:
            u = stjump[u][p]
            v = stjump[v][p]
    
    if u==v:
        return u
    return stjump[u][0]

def path_hash(from_node,lca_node,to_node):
    up = s[from_node]
    for p in range(power,-1,-1):
        if deep[stjump[from_node][p]]>=deep[lca_node]:
            up = up*kpow[1<<p] + stup[from_node][p]
            from_node = stjump[from_node][p]
    
    if to_node==lca_node:
        return up
    
    down = s[to_node]
    h = 1
    for p in range(power,-1,-1):
        if deep[stjump[to_node][p]]>deep[lca_node]:
            down = stdown[to_node][p]*kpow[h] + down
            h+=1<<p
            to_node = stjump[to_node][p]
    
    return up*kpow[h] + down

def is_palindrome(a, b):
    l = lca(a, b)
    return path_hash(a, l, b) == path_hash(b, l, a)


# ================= 主程序 =================
n = int(input())
build(n)

chars = input().strip()
for i in range(n):
    s[i + 1] = ord(chars[i]) - ord('a') + 1

for u in range(1, n + 1):
    v = int(input())
    g[u].append(v)
    g[v].append(u)

dfs(1, 0)

m = int(input())
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    ans.append("YES" if is_palindrome(a, b) else "NO")

print("\n".join(ans))