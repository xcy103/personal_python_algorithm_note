#猪头了，算一个后缀最大lcp，求答案的时候维护一个前缀lcp
@cache  # 避免重复计算
def lcp(s: str, t: str) -> int:
    cnt = 0
    for x, y in zip(s, t):
        if x != y:
            break
        cnt += 1
    return cnt

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        ans = [0] * n
        if n == 1:  # 不存在相邻对
            return ans

        # 后缀 [i,n-1] 中的相邻 LCP 长度的最大值
        suf_max = [0] * n
        for i in range(n - 2, 0, -1):
            suf_max[i] = max(suf_max[i + 1], lcp(words[i], words[i + 1]))

        ans[0] = suf_max[1]
        pre_max = 0  # 前缀 [0,i-1] 中的相邻 LCP 长度的最大值
        for i in range(1, n - 1):
            ans[i] = max(pre_max, lcp(words[i - 1], words[i + 1]), suf_max[i + 1])
            pre_max = max(pre_max, lcp(words[i - 1], words[i]))  # 为下一轮循环做准备
        ans[-1] = pre_max
        return ans