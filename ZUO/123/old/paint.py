# 染色的最大收益
# 给定一棵n个点的树，初始时所有节点全是白点
# 第一次操作，你可以选择任意点染黑
# 以后每次操作，必须选择已经染黑的点的相邻点继续染黑，一直到所有的点都被染完
# 每次都获得，当前被染色点的白色连通块大小，作为收益
# 返回可获得的最大收益和
# 测试链接 : https://www.luogu.com.cn/problem/CF1187E

# 这个有点难想
# 应该从两个视角去看。第一个视角是先染V，这个时候U是后染的，所以比之前多了n-size[V]的收益，
# 第二个视角是后染U，这时候V已经染色了，缺了size[V]的收益。这两个视角都是和之前比的

def solve():
  
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    n = int(input_data[ptr])
    ptr += 1

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input_data[ptr:ptr + 2])
        ptr += 2
        g[u].append(v)
        g[v].append(u)
    
    size = [0] * (n + 1)
    dp = [0] * (n + 1)
    
    def dfs1(u,f):
        size[u] = 1
        for v in g[u]:
            if v!=f:
                dfs1(v,u)
                size[u]+=size[v]
                dp[u] += dp[v]
        dp[u] += size[u]
    
    def dfs2(u,f):
        for v in g[u]:
            if v!=f:
                dp[v] = dp[u] + n - 2 * size[v]
                dfs2(v,u)
    
    dfs1(1,0)
    dfs2(1,0)
    print(max(dp))

if __name__ == "__main__":
    solve()

