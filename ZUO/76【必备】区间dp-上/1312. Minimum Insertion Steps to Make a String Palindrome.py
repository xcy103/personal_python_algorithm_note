# 感觉区间DP最大的难点是，，，状态定义
# 就是你不知道怎么定义状态
# 这道题就是比较左右两端点，如果相等左加1右减一
# 如果不相等，左加1或者右减一，取最小值
# 区间dp：大范围的问题拆分成若干小范围的问题来求解

# 可能性展开的常见方式：
# 1）基于两侧端点讨论的可能性展开
# 2）基于范围上划分点的可能性展开
#  让字符串成为回文串的最少插入次数
#  给你一个字符串 s
#  每一次操作你都可以在字符串的任意位置插入任意字符
#  请你返回让s成为回文串的最少操作次数
#  测试链接 : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s = list(s)
        @cache
        def f(i,j):
            if i==j:
                return 0
            if i+1==j:
                return 0 if s[i]==s[j] else 1
            if s[i]==s[j]:
                return f(i+1,j-1)
            return min(f(i+1,j),f(i,j-1))+1
        return f(0,n-1)