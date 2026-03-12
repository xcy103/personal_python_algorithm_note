#蠢货，枚举所有汇聚点。
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for [u,v,w] in edges:
            g[u].append((v,w))
            rg[v].append((u,w))
        
        def dijsktra(start,g):
            dis = [inf]*n
            h = []
            dis[start] = 0
            heappush(h,(0,start))
            while h:
                w,x = heappop(h)
                if dis[x]<w:
                    continue
                
                for [y,c] in g[x]:
                    if dis[y]>w+c:
                        dis[y] = w+c
                        heappush(h,(dis[y],y))
            return dis
        
        d1 = dijsktra(src1,g)
        d2 = dijsktra(src2,g)
        d3 = dijsktra(dest,rg)
        ans = inf
        for i in range(n):
            ans = min(ans,d1[i] + d2[i] + d3[i])
        return -1 if ans==inf else ans