#这里面的题目都是贪心算法，都含有不同的技巧，需要掌握
#这道题是字符串拼接比较,对于两个数 x 和 y，比较 x+y 和 y+x，谁大谁在前。


from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 转成字符串
        nums = list(map(str, nums))
        
        # 自定义比较函数
        def cmp(x, y):
            if x + y > y + x:
                return -1  # x 应该在前
            elif x + y < y + x:
                return 1   # y 在前
            else:
                return 0
        
        # 排序
        nums.sort(key=cmp_to_key(cmp))
        
        # 拼接结果
        res = ''.join(nums)
        
        # 处理全是0的情况
        return '0' if res[0] == '0' else res