# 换根DP入门题

# 树上的某些问题，需要知道以不同的节点做根的情况下，答案是多少

# 换根dp的思考重点
# 如果已经得到父节点做根的答案，怎么加工得到子节点做根的答案，
# 就是所谓的换根为了达成换根这个目标，可能需要设置若干额外的信息来帮助计算

# 换根dp的过程
# 1，先以节点1为头进行树的遍历，收集信息，dfs1过程
# 2，得到1节点做根的答案，然后从1节点开始再进行树的遍历，
#    求解每个节点做根的答案，dfs2过程核心在于换根时，答案如何转移

def solve(n, edges):
    """
    n: 节点数量 (int)
    edges: 边列表，例如 [(1, 2), (2, 3), ...]
    return: 能使深度和最大的节点编号 (int)
    """

    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    
    size =  [0] * (n + 1)
    deep_sum = [0] * (n + 1)
    dp = [0] * (n + 1)

    def dfs1(u,f):
        size[u] = 1
        deep_sum[u] = 0
        for v in g[u]:
            if v!=f:
                dfs1(v,u)
                size[u]+=size[v]
                deep_sum[u]+=deep_sum[v]+size[v]
    
    def dfs2(u,f):
        for v in g[u]:
            if v!=f:
                dp[v] = dp[u] - size[v] + n - size[v]
                dfs2(v,u)
    dfs1(1,0)
    dp[1] = deep_sum[1]
    dfs2(1, 0)

    ans = 1
    mx = dp[1]
    for i in range(2,n+1):
        if dp[i]>mx:
            mx = dp[i]
            ans = i
    return ans