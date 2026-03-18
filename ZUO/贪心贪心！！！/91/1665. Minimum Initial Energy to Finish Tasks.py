#  执行所有任务的最少初始电量
#  每一个任务有两个参数，需要耗费的电量、至少多少电量才能开始这个任务
#  返回手机至少需要多少的初始电量，才能执行完所有的任务
#  测试链接 : https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/

#这道题用到了交换论证

"""
【贪心策略交换论证总结】 - LeetCode 1665: 完成所有任务的最少初始能量

1. 贪心策略：
按照 (minimum - actual) 的差值降序排列任务。

2. 交换论证 (Exchange Argument) 证明：
假设有相邻的两个任务 A 和 B：
- 任务 A：消耗 a1，门槛 m1
- 任务 B：消耗 a2，门槛 m2

执行顺序所需的最少初始能量：
- 先 A 后 B (E_ab): 先满足 A 的门槛，做完后剩余能量需满足 B 的门槛。
  公式: E_ab = max(m1, m2 + a1)
- 先 B 后 A (E_ba): 同理。
  公式: E_ba = max(m2, m1 + a2)

3. 核心推导：
假设按照我们的贪心策略，A 排在 B 前面，即满足：
m1 - a1 >= m2 - a2
移项得到核心不等式：
m1 + a2 >= m2 + a1

我们来观察 先 B 后 A 的能量需求 E_ba = max(m2, m1 + a2)：
- 已知 m1 + a2 >= m2 + a1 (核心不等式)
- 已知 m1 + a2 >= m1 (因为消耗能量 a2 >= 0)

由此可见，m1 + a2 必定大于等于 m1 和 (m2 + a1)。
因此：
max(m2, m1 + a2) >= max(m1, m2 + a1)
即：E_ba >= E_ab

4. 结论：
只要相邻两项满足 (m1 - a1 >= m2 - a2)，先执行 A 永远不会比先执行 B 需要的初始能量更多。
通过不断交换“逆序”的相邻任务，总能量需求只会减少或不变，从而证明该贪心排序即为全局最优解。
"""
#就是，如果发现，两个指标互相矛盾，比如这道题，耗费希望越大越好，至少希望越小越好，
#那么一般就要两个指标结合来看，做差什么的
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)

        energy = 0
        cur = 0

        for actual, minimum in tasks:
            
            if cur < minimum:
                energy += minimum - cur
                cur = minimum
            
            cur -= actual

        return energy
#更简单的
# class Solution:
#     def minimumEffort(self, tasks: List[List[int]]) -> int:
        
#         tasks.sort(key=lambda x: x[1]-x[0])

#         ans = 0
#         for i in range(len(tasks)):
#             ans = max(tasks[i][1],ans+tasks[i][0])
        
#         return ans