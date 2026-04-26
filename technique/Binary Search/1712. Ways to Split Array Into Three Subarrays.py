from bisect import bisect_left, bisect_right
from itertools import accumulate
#坐牢了100分钟。。。。
class Solution:
    def waysToSplit(self, nums):
        pre = [0] + list(accumulate(nums))
        n = len(nums)
        mod = 10**9 + 7
        ans = 0
        
        for i in range(1, n-1):
            if pre[-1] < 3 * pre[i]:
                break
            
            # 左边界
            l = bisect_left(pre, 2 * pre[i], i+1, n)
            
            # 右边界（注意用 bisect_right）
            r = bisect_right(pre, (pre[-1] + pre[i]) // 2, i+1, n)
            
            if l < r:
                ans = (ans + (r - l)) % mod
        
        return ans