#  到达首都的最少油耗
#  给你一棵 n 个节点的树（一个无向、连通、无环图）
#  每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路
#  0 是首都。给你一个二维整数数组 roads
#  其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路
#  每个城市里有一个代表，他们都要去首都参加一个会议
#  每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目
#  城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车
#  相邻城市之间一辆车的油耗是一升汽油
#  请你返回到达首都最少需要多少升汽油
#  测试链接 : https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution:
    def minimumFuelCost(self, roads, seats):
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)

        ans = 0

        def dfs(u, parent):
            nonlocal ans
            people = 1  # 当前节点1个人

            for v in g[u]:
                if v != parent:
                    p = dfs(v, u)
                    ans += (p + seats - 1) // seats
                    people += p #注意，还要收集子树的人，汇聚到当前节点

            return people

        dfs(0, -1)
        return ans