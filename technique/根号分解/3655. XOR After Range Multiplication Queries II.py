# 设定 MOD = 1e9+7，B = sqrt(queries数量)，n = nums长度
# 创建 groups，按步长 k 分组，小于 B 的放入 groups[k]
# 遍历 queries：
# 如果 k >= B：直接暴力枚举 i = l 到 r，步长 k，更新 nums[i]
# 如果 k < B：加入对应 groups[k]
# 处理每个 k（0 到 B-1）：
# 如果该组为空，跳过
# 按照起点模 k 分桶 buckets[start]
# 对每个 bucket（相同 start % k）：
# 如果只有一个区间，直接暴力更新
# 如果有多个区间：
# a. 计算该等差序列长度 m
# b. 建立差分数组 diff，初始化为1
# c. 对每个区间(l,r,v)：
# diff[l//k] *= v
# diff[(r-start)//k + 1] = v的逆元
# d. 前缀积恢复真实倍率
# e. 更新 nums[start + ik]
# 最后对 nums 所有元素做异或，返回结果


from math import isqrt
from functools import reduce
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        B = isqrt(len(queries))
        n = len(nums)
        groups = [[] for _ in range(B)]

        for l,r,k,v in queries:
            if k<B:
                groups[k].append((l,r,v))
            else:
                for i in range(l,r+1,k):
                    nums[i] = nums[i]*v%MOD
        
        for k,g in enumerate(groups):
            if not g:
                continue
            buckets = [[] for _ in range(k)]
            for t in g:
                buckets[t[0]%k].append(t)

            for start,bucket in enumerate(buckets):
                if not bucket:continue
                if len(bucket)==1:
                    l,r,v = bucket[0]
                    for i in range(l,r+1,k):
                        nums[i] = nums[i]*v%MOD
                    continue
                m = (n-start-1)//k+1
                diff = [1]*(m+1)
                for l,r,v in bucket:
                    diff[l//k] = diff[l//k]*v%MOD
                    r = (r-start)//k + 1
                    diff[r] = diff[r]*pow(v,-1,MOD)%MOD
                res = 1
                for i in range(m):
                    res = res*diff[i]%MOD
                    j = start + i*k
                    nums[j] = nums[j]*res%MOD
        return reduce(xor,nums)