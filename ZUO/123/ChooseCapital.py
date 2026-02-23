# 这里的逻辑是，首先找出dp1的代价
# 就是以1为首都去往所有城市代价，处理边的时候我们可以
# 正向边代价为0，反向边代价为1
# dp的递推逻辑是，来到子节点，现在要去父结点
# 因为dp[父]包含了去往所有子节点的代价，包括了
# 来到现在我们在的子节点，然后再从现在这个子节点去往
# 子节点其他子树的代价，以及父节点去往其他子节点的代价，
# 所以现在的关键只有一条边，就是父节点去往现在的子节点的
# 这条边，如果这条边是正向，从父到子，那么现在，我们需要从子到父
# 所以我们需要多付出1的代价
# 反之，如果这条边是从父到子，说明dp[父]中已经包含了这条边，
# 所以现在可以少付出1的代价
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

while True:
    line = input()
    if not line:break
    n = int(line)

    g = [[] for _ in range(n+1)]

    for _ in range(n-1):
        u,v = map(int,input().split())
        g[u].append((v,0))
        g[v].append((u,1))

    reverse = [0]*(n+1)
    dp = [0]*(n+1)

    def dfs1(u,f):
        for v,w in g[u]:
            if v==f:
                continue
            dfs1(v,u)
            reverse[u]+=reverse[v]+w

    def dfs2(u,f):
        for v,w in g[u]:
            if v==f:continue
            if w==0:
                dp[v] = dp[u] - 1
            else:
                dp[v] = dp[u] + 1
            dfs2(v,u)
    
    dfs1(1,0)
    dp[1] = reverse[1]
    dfs2(1,0)

    mn = min(dp[1:])
    print(mn)
    for i in range(1, n + 1):
        if dp[i] == mn:
            print(i, end=" ")
    print()
