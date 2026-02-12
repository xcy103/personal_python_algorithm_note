# 树上差分加树形DP
#  最小化旅行的价格总和(倍增方法求lca)
#  有n个节点形成一棵树，每个节点上有点权，再给定很多路径
#  每条路径有开始点和结束点，路径代价就是从开始点到结束点的点权和
#  所有路径的代价总和就是旅行的价格总和
#  你可以选择把某些点的点权减少一半，来降低旅行的价格总和
#  但是要求选择的点不能相邻
#  返回旅行的价格总和最少能是多少
#  测试链接 : https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
def minimumTotalPrice(
    self,
    n: int,
    edges: List[List[int]],
    price_list: List[int],
    trips: List[List[int]]
) -> int:

    # ---------- 1-based ----------
    price = [0] * (n + 1)
    for i in range(n):
        price[i + 1] = price_list[i]

    # ---------- 建树 ----------
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        u += 1
        v += 1
        g[u].append(v)
        g[v].append(u)

    # ---------- LCA 预处理 ----------
    LOG = (n + 1).bit_length()
    depth = [0] * (n + 1)
    parent = [[0] * LOG for _ in range(n + 1)]

    def dfs1(u: int, f: int):
        depth[u] = depth[f] + 1
        parent[u][0] = f
        for k in range(1, LOG):
            parent[u][k] = parent[parent[u][k - 1]][k - 1]
        for v in g[u]:
            if v != f:
                dfs1(v, u)

    dfs1(1, 0)

    def lca(a: int, b: int) -> int:
        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]
        k = 0
        while diff:
            if diff & 1:
                a = parent[a][k]
            diff >>= 1
            k += 1

        if a == b:
            return a

        for k in range(LOG - 1, -1, -1):
            if parent[a][k] != parent[b][k]:
                a = parent[a][k]
                b = parent[b][k]

        return parent[a][0]

    # ---------- 树上点差分 ----------
    num = [0] * (n + 1)

    for u, v in trips:
        u += 1
        v += 1
        c = lca(u, v)
        num[u] += 1
        num[v] += 1
        num[c] -= 1
        if parent[c][0]:
            num[parent[c][0]] -= 1

    # ---------- DFS 汇总 ----------
    def dfs2(u: int, f: int):
        for v in g[u]:
            if v != f:
                dfs2(v, u)
                num[u] += num[v]

    dfs2(1, 0)

    # ---------- 树形 DP ----------
    # no : 不减半
    # yes: 减半
    def dp(u: int, f: int):
        no = price[u] * num[u]
        yes = (price[u] // 2) * num[u]
        for v in g[u]:
            if v != f:
                cn, cy = dp(v, u)
                no += min(cn, cy)
                yes += cn
        return no, yes

    no, yes = dp(1, 0)
    return min(no, yes)