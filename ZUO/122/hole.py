# 二分答案（最大耗时），利用 LCA 快速求出路径长度，并通过 树上差分 在 $O(n)$ 时间内判断
# 是否存在一条被所有“超标路径”共同覆盖的边，将其权值置零后能使所有路径满足限制。
#  有n个节点，给定n-1条边使其连接成一棵树，每条边有正数边权
#  给定很多运输计划，每个运输计划(a,b)表示从a去往b
#  每个运输计划的代价就是沿途边权和，运输计划之间完全互不干扰
#  你只能选择一条边，将其边权变成0
#  你的目的是让所有运输计划代价的最大值尽量小
#  返回所有运输计划代价的最大值最小能是多少
#  测试链接 : https://www.luogu.com.cn/problem/P2680
def solve(n,m,edges,plans):
    """
    n: 节点数量 (int)
    m: 计划数量 (int)
    edges: 边列表，每个元素为 (u, v, w)
    plans: 运输计划列表，每个元素为 (u, v)
    return: 所有运输计划代价的最大值最小能是多少
    """
    # 1. 建图 (邻接表)
    g = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    
    # 2. 预处理数据结构
    # query_adj 用于 Tarjan 算法
    query_adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u,v = plans[i]
        query_adj[u].append((v,i))
        query_adj[v].append((u,i))
    
    # 并查集数组
    uf = [i for i in range(n + 1)]
    vis = [False]*(n+1)
    # 记录每个节点到根节点(1号点)的距离
    dist = [0]*(n+1)

    # 存储结果
    lca_res = [0]*m
    cost_res = [0]*m

    def find(x):
        if uf[x] != x: uf[x] = find(uf[x])
        return uf[x]

    #Trajan算法
    def tarjan(u,f,w):
        vis[u] = True
        dist[u] = dist[f] + w

        for v,vw in g[u]:
            if not vis[v]:
                tarjan(v,u,vw)
                uf[v] = u
        for v,idx in query_adj[u]:
            if vis[v]:
                lca = find(v)
                lca_res[idx] = lca
                cost_res[idx] = dist[u] + dist[v] - 2*dist[lca]
        
    tarjan(1,0,0)

    max_dist_all = 0
    if m > 0:
       max_dist_all = max(cost_res)
    # -----------------------------------------------------------
    # 优化：为了避免在二分 check 时的递归 (Java中的 dfs)，
    # 我们预处理出 BFS 序（拓扑序），用于后续自底向上进行差分求和。
    # 这样就把 check 函数变成了纯迭代，性能极高。
    # -----------------------------------------------------------

    bfs_order = []
    parent = [0]*(n+1)
    w_to_parent = [0]*(n+1)
    q = [1]
    vis_bfs = [False]*(n+1)
    vis_bfs[1] = True

    while q:
        u = q.pop(0)
        bfs_order.append(u)
        for v,w in g[u]:
            if not vis_bfs[v]:
                parent[v] = u
                w_to_parent[v] = w
                q.append(v)
                vis_bfs[v] = True
    
    # bfs_order 的逆序即为从叶子到根的顺序
    bfs_order.reverse()
    # 差分数组，这里只需要分配一次内存，反复使用
    diff = [0]*(n+1)

    # 二分
    def check(limit):
        # 1. 找出所有超过 limit 的计划
        # 目标：需要找到一条边，被所有“超标计划”经过，且权值足够大

        target = max_dist_all - limit
        beyond = 0

        # 清空差分数组
        for i in range(n + 1):
            diff[i] = 0
        
        for i in range(m):
            if cost_res[i] > target:
                beyond += 1
                u,v = plans[i]
                anc =  lca_res[i]
                diff[u] += 1
                diff[v] += 1
                diff[anc] -= 2
        # 如果没有超标的，直接成功
        if beyond == 0:
            return True
        
        # 2. 自底向上求和 (替代递归 DFS)
        # 遍历除了根节点以外的所有点
        for u in bfs_order:
            if u==1: continue
            p = parent[u]
            diff[p] += diff[u]

            # 检查连接 u 和 p 的这条边
            # 条件1: 这条边被所有超标路径覆盖 (diff[u] == beyond_cnt)
            # 条件2: 这条边的权值 >= 需要减少的量
            if diff[u] == beyond and w_to_parent[u] >= target:
                return True

        return False
    
    #3 二分答案主体
    l,r = 0,max_dist_all+1
    while l+1<r:
        mid = (l+r)//2
        if check(mid): r = mid
        else: l = mid
    return l#或者r每次都不知道返回哪个