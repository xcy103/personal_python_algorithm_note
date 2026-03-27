#  相邻字符不同的最长路径
#  给你一棵 树（即一个连通、无向、无环图），根节点是节点 0
#  这棵树由编号从 0 到 n - 1 的 n 个节点组成
#  用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树
#  其中 parent[i] 是节点 i 的父节点
#  由于节点 0 是根节点，所以 parent[0] == -1
#  另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符
#  请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径
#  并返回该路径的长度
#  测试链接 : https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# 整体思路就是，选取经过a的最长链，当然可能也不经过a，但是我们的情况包含了
# 不经过a，但是肯定经过某一个节点，但是我们还是收集答案了
class Solution:
    def longestPath(self, p: List[int], s: str) -> int:
        n = len(p)
        g = [[] for _ in range(n)]
        for i in range(1,n):
            g[p[i]].append(i)
        if n==1:
            return 1
        ans = 0
        def f(a):
            nonlocal ans
            x = 0
            for b in g[a]:
                y = f(b)
                if s[a]!=s[b]:
                    ans = max(x+y,ans)
                    x = max(x,y)
            return x+1
        f(0)
        return ans+1
