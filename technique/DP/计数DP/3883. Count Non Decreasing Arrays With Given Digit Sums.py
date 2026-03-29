# 这道题怎么思考呢，预处理我知道
# 这道题要求是非递减数组，我刚开始想的是
# 来到一位，循环这一位，然后搞一个pre记录，再去下一位
# 但是这样会超时
# 这道题本质是是二分DP，计数DP，前缀和优化
# dp[i][j]的含义是，在第i个位置，选下标为j的数，满足条件的方案数
# 怎么转移呢,我们看i-1位置的数，假设是a，那么i位置的数必须大于等于a
# 因为预处理的数是有序的，所以我们可以二分找到a在i位置的数中最大的下标k，那么dp[i][j]就等于dp[i-1][0]+...+dp[i-1][k]
# 这样就可以用前缀和优化了，pre[j] = dp[i-1][0]+...+dp[i-1][j]
from collections import defaultdict
import bisect

MOD = 10**9+7

# 预处理
d = defaultdict(list)
for i in range(5001):
    s = sum(map(int, str(i)))
    d[s].append(i)


def countArrays(digitSum):
    n = len(digitSum)
    
    # 提前判空
    for s in digitSum:
        if not d[s]:
            return 0
    
    prev = [1] * len(d[digitSum[0]])
    
    for i in range(1, n):
        a = d[digitSum[i-1]]
        b = d[digitSum[i]]
        
        if not a or not b:
            return 0
        
        pre = [0] * len(a)
        pre[0] = prev[0]
        for j in range(1, len(a)):
            pre[j] = (pre[j-1] + prev[j]) % MOD
        
        cur = [0] * len(b)
        
        for j in range(len(b)):
            k = bisect.bisect_right(a, b[j]) - 1
            if k >= 0:
                cur[j] = pre[k]
        
        prev = cur
    
    return sum(prev) % MOD

countArrays([22,14,14,18])