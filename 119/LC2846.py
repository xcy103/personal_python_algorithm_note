class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MAXW = 26
        g = [[] for _ in range(n)]

        for u,v,w  in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        wc = [[0]*(MAXW+1) for _ in range(n)]
        #统计边的数量
        def dfs(u,f):
            for v,w in g[u]:
                if v!=f:
                    for i in range(1,MAXW+1):
                        wc[v][i] = wc[u][i]
                    wc[v][w]+=1
                    dfs(v,u)
        dfs(0,-1)

        #trajan离线处理lca
        q = len(queries)
        qg = [[] for _ in range(n)]
        for i,(a,b) in enumerate(queries):
            qg[a].append((b,i))
            qg[b].append((a,i))
        
        f = list(range(n))
        vis = [False]*n
        lca = [0]*q

        def find(x):
            if f[x]!=x:
                f[x] = find(f[x])
            return f[x]
        
        def tarjan(u,fa):
            vis[u] = True
            for v,_ in g[u]:
                if v!=fa:
                    tarjan(v,u)
            for v,idx in qg[u]:
                if vis[v]:
                    lca[idx] = find(v)
            f[u] = fa
        
        tarjan(0,-1)

        #最后的求解
        ans = [0]*q
        for i,(a,b) in enumerate(queries):
            c = lca[i]
            total = 0
            mx = 0
            for w in range(1,MAXW+1):
                cnt = wc[a][w]+wc[b][w] - 2*wc[c][w]
                total+=cnt
                mx = max(mx,cnt)
            ans[i] = total - mx
        return ans
