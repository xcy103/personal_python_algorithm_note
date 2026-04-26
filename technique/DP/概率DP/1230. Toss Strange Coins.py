class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0.0] * (target + 1)
        dp[0] = 1.0
        
        for p in prob:
            # ⚠️ 必须倒序！
            for j in range(target, -1, -1):
                if j == 0:
                    dp[j] = dp[j] * (1 - p)
                else:
                    dp[j] = dp[j] * (1 - p) + dp[j - 1] * p
        
        return dp[target]