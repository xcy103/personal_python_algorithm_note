#我知道可以用dijskra求最短路，但是不知道怎么求答案，差很多
#求出之后就可以树上暴力搜索，题目给了每个点最多4条边
#只有回到0点才更新答案
class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        from heapq import heappush, heappop
        n = len(values)

        g = [[] for _ in range(n)]
        for u,v,t in edges:
            g[u].append((v,t))
            g[v].append((u,t))

        # Dijkstra 求到0的最短路
        dist = [float('inf')]*n
        dist[0] = 0
        h = [(0,0)]

        while h:
            d,x = heappop(h)
            if d>dist[x]:
                continue
            for y,w in g[x]:
                if dist[y] > d+w:
                    dist[y] = d+w
                    heappush(h,(dist[y],y))

        ans = 0
        vis = [0]*n

        def dfs(x,time,score):
            nonlocal ans

            if x==0:
                ans = max(ans,score)

            for y,w in g[x]:
                nt = time + w

                if nt + dist[y] > maxTime:
                    continue

                add = 0
                if vis[y]==0:
                    add = values[y]

                vis[y]+=1
                dfs(y,nt,score+add)
                vis[y]-=1

        vis[0] = 1
        dfs(0,0,values[0])

        return ans