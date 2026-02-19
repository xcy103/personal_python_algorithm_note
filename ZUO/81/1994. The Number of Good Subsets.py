from typing import List
# 这道题和左老师思路不同，首先预处理阶段是相同的
# 先用位信息表示2-30的质因数分解情况
# 但是用了01背包，先判断一个数是否在这个集合里以及这个数是否合法
# 然后倒序枚举状态，如果我们选的数可以放进状态，我们就更新dp数组
# 快速枚举所有子集
# j = status
# while j:
#     # 处理子集j
#     j = (j-1) & status
MOD = 10**9+7
MAXV = 30
primes = [2,3,5,7,11,13,17,19,23,29]
own = [0]*(MAXV+1)
for i in range(2,MAXV+1):
    mask = 0
    temp = i
    f = 1
    for j,p in enumerate(primes):
        if temp%p == 0:
            cnt = 0
            while temp%p==0:
                cnt+=1
                temp//=p
            if cnt>1:
                f = 0
                break
            mask|=1<<j
    if f:
        own[i] = mask

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        
        
        cnt = [0]*(MAXV+1)
        for x in nums:
            cnt[x]+=1
        
        LIMIT = 1<<10
        dp = [0]*LIMIT
        dp[0] = pow(2,cnt[1],MOD)

        for i in range(2,MAXV+1):
            c = cnt[i]
            mask = own[i]
            if c==0 or mask ==0 :
                continue
            
            for status in range(LIMIT-1,-1,-1):
                if status&mask==0:
                    new_mask = status | mask
                    dp[new_mask] = (dp[new_mask] + dp[status]*c)%MOD
        return sum(dp[1:])%MOD