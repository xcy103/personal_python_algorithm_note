#  每个节点距离k以内的权值和(递归版)
#  给定一棵n个点的树，每个点有点权
#  到达每个节点的距离不超过k的节点就有若干个
#  把这些节点权值加起来，就是该点不超过距离k的点权和
#  打印每个节点不超过距离k的点权和
#  注意k并不大
#  测试链接 : https://www.luogu.com.cn/problem/P3047

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    n = int(input_data[ptr])
    k = int(input_data[ptr + 1])
    ptr+=2

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input_data[ptr:ptr + 2])
        ptr += 2
        g[u].append(v)
        g[v].append(u)
    
    # sum_val[u][i]: u子树内距离u为i的权值和
    # dp[u][i]: 全树中距离u为i的权值和

    sum_val = [[0] * (k + 1) for _ in range(n + 1)]
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        sum_val[i][0] = int(input_data[ptr])
        ptr += 1
    
    #第一遍DFS：自底向上统计子树贡献
    def dfs1(u,f):
        for v in g[u]:
            if v==f:
                continue
            dfs1(v,u)
            for j in range(1,k+1):
                sum_val[u][j] += sum_val[v][j-1]
    
    def dfs2(u,f):
        for v in g[u]:
            if v!=f:
                dp[v][0] = sum_val[v][0]
                dp[v][1] = sum_val[v][1] + dp[u][0]
                for j in range(2,k+1):
                    dp[v][i] = sum[v][i] + dp[u][i-1] - sum[v][i-2]

                dfs2(v,u)
    
    dfs1(1,0)

    for i in range(k+1):
        dp[1][i] = sum_val[1][i]
    

    dfs2(1,0)
    out = []
    for i in range(1,n+1):
        out.append(str(sum(dp[i])))
    
    sys.stdout.write("\n".join(out) + "\n" )

if __name__ == "__main__":
    solve()