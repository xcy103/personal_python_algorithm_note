import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    size = [0] * (n + 1)
    maxsub = [0] * (n + 1)

    def dfs(u,f):
        size[u] = 1
        maxsub[u] = 0
        for v in graph[u]:
            if v == f:
                continue
            dfs(v, u)
            size[u] += size[v]
            maxsub[u] = max(maxsub[u], size[v])
        
        maxsub[u] = max(maxsub[u], n - size[u])

    dfs(1,0)
    centers = []
    for i in range(1, n + 1):
        if maxsub[i] <= n // 2:
            centers.append(i)
    
    if len(centers)==1:
        c = centers[0]
        v = graph[c][0]
        print(c, v)
        print(c, v)
    else:
        # 两个重心
        c1, c2 = centers[0], centers[1]
        
        # 在 c2 子树中找一个叶子（不能往 c1 走）
        leaf = -1
        leafFather = -1
        def find_leaf(u,f):
            global leaf, leafFather
            for v in graph[u]:
                if v == f:
                    continue
                find_leaf(v, u)
            leaf = u
            leafFather = f
            
        find_leaf(c2, c1)
        
        # 删 leafFather - leaf
        print(leafFather, leaf)
        # 加 c1 - leaf
        print(c1, leaf)