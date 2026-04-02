#这道题其实限制theshold没用，
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        g= [[] for _ in range(n)]
        for u,v,w in edges:
            g[v].append((u,w))
        
        def check(x):
            vis = [False]*n
            st = [0]
            vis[0] = True
            while st:
                u = st.pop()
                for v,w in g[u]:
                    if w<=x and not vis[v]:
                        vis[v] = True
                        st.append(v)
                        
            return all(vis)
        l = 0
        r = 10**6+1
        while l+1<r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid
        return r if r!=10**6+1 else -1