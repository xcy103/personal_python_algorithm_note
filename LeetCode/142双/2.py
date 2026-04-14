from collections import Counter
from itertools import pairwise
def findSubtreeSizes( parent,s: str):
        #感觉很简单，就是从底到顶收集26个字母，最后的答案就是自己的子树有多少个和自己相同的字母
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1,n):
            g[parent[i]].append(i)
        for x,y in pairwise(g):
            print(x,y)  
        print(g)
        s = list(s)
        size = [0]*n
        def dfs(u,fa,pre):
            pre.add(s[u])
            nonlocal size
            if len(g[u])==0:
                c = Counter()
                c[s[u]]+=1
                size[u] = 1
                return c
            c = Counter()
            c[s[u]]+=1
            for v in g[u]:
                if v==fa:continue
                c+=dfs(v,u,pre.copy())
            size[u] = c[s[u]]
            for ch in c.keys():
                if ch not in pre:
                    size[u]+=c[ch]
            return c
        dfs(0,-1,set())
        size[0] = n
        return size
findSubtreeSizes([-1,0,0,1,1,1],"abaabc")