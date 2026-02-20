# 这道题不可以用贪心，比如[1,1,1,2,2],quantity=[2,3]，如果我们先满足订单2，剩下的1只能满足订单1的一个，结果是失败的
# 我们可以先统计数字的频率，然后对订单的状态进行状态压缩DP
# 循环遍历每一个数字，当来到一个数字
# 我们遍历每个用户被满足的状态，如果这个数字可以让某一些用户满足，
# 我们就可以来到下一个数字，剔除被满足的用户，然后进行相同的操作
# 如果都是1了，就返回True，如果用户状态遍历完了，ans是False
# 说明这个数字不能带来什么进展，继续递归到下一个数字
from collections import Counter
from functools import lru_cache
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # 1. 统计频率：我们只关心数字出现的次数，不关心数字本身
        cnt = Counter(nums)
        freq = list(cnt.values())
        
        # 2. 排序优化：大的订单先处理，能显著提高枚举时的剪枝效率
        quantity.sort(reverse=True)
        n = len(quantity)
        
        # 3. 预处理：计算订单 quantity 的每一个子集状态 mask 所需的总量
        # count[mask] 表示满足该集合所有订单需要的数字个数
        sub_sum = [0] * (1 << n)
        for i in range(n):
            bit = 1 << i
            val = quantity[i]
            for mask in range(bit):
                sub_sum[bit | mask] = sub_sum[mask] + val
        
        m = len(freq)

        @lru_cache(None)
        def dfs(mask, i):
            # mask 为当前还未满足的订单集合（1表示未满足）
            if mask == 0:
                return True
            # 数字频率用完了，但订单还没满
            if i == m:
                return False
            
            # 情况 1: 当前这个频率 freq[i] 一个订单都不接
            if dfs(mask, i + 1):
                return True
            
            # 情况 2: 枚举 mask 的所有子集 sub
            # 尝试让 freq[i] 承接子集 sub 对应的订单
            sub = mask
            while sub > 0:
                if sub_sum[sub] <= freq[i]:
                    # 如果能承接，递归看剩下的订单 mask ^ sub
                    if dfs(mask ^ sub, i + 1):
                        return True
                # 枚举下一个子集的位运算技巧
                sub = (sub - 1) & mask
                
            return False

        # 初始状态：所有订单都未满足 (1<<n)-1，从第 0 个频率开始看
        return dfs((1 << n) - 1, 0)