from typing import List
from math import inf

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = n // k
        
        nums.sort()
        
        # 如果某个数出现次数 > k，必不可能
        from collections import Counter
        cnt = Counter(nums)
        if any(v > k for v in cnt.values()):
            return -1
        
        # 预处理所有合法子集
        size = 1 << n
        cost = [-1] * size
        
        for mask in range(size):
            if mask.bit_count() != m:
                continue
            
            seen = set()
            mx = -1
            mn = 10**9
            valid = True
            
            for i in range(n):
                if mask & (1 << i):
                    if nums[i] in seen:
                        valid = False
                        break
                    seen.add(nums[i])
                    mx = max(mx, nums[i])
                    mn = min(mn, nums[i])
            
            if valid:
                cost[mask] = mx - mn
        
        # 状压DP
        dp = [inf] * size
        dp[0] = 0
        
        for mask in range(size):
            if dp[mask] == inf:
                continue
            
            remain = (~mask) & (size - 1)
            
            # 优化：如果剩余数量不是 m 的倍数，跳过
            if remain.bit_count() % m != 0:
                continue
            
            sub = remain
            while sub:
                if cost[sub] != -1:
                    dp[mask | sub] = min(
                        dp[mask | sub],
                        dp[mask] + cost[sub]
                    )
                sub = (sub - 1) & remain
        
        ans = dp[size - 1]
        return ans if ans != inf else -1
