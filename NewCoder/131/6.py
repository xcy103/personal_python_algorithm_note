import sys

t = int(input())
mod = 998244353
res = []
for _ in range(t):
    n = int(input())
    s = list(input().split()[0])
    g = [[] for _ in range(n)]
    st = []

    for i,ch in enumerate(s):
        if ch=='(':
            if st:
                g[st[-1]].append(i)
                g[i].append(st[-1])
            st.append(i)
        else:
            g[st[-1]].append(i)
            g[i].append(st[-1])
            if st[-1]+1!=i:
                g[i-1].append(i)
                g[i].append(i-1)
            st.pop()
    vis = [False]*n
    op = 0
    def dfs(u,f):
        vis[u] = True
        for v in g[u]:
            if v==f or vis[v]:continue
            dfs(v,u)
    for i in range(n):
        if not vis[i]:
            op+=1
            dfs(i,-1)
    res.append(str(pow(2,op,mod)))

print('\n'.join(res))

