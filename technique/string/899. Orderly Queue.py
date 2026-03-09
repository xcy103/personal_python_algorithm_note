# 求字符串循环同构串中字典序最小者。
# 通过双指针维护候选起点，每次排除 k+1 个位置，总复杂度 O(n)。
# 模板题为 899. 有序队列（k=1）。
# 对于这道题有贪心结论，K==1就是环，找最小，k>=2可以直接sort返回

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        
        return ''.join(sorted(s))
