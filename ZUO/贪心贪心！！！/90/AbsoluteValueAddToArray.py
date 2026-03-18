#  加入差值绝对值直到长度固定
#  给定一个非负数组arr，计算任何两个数差值的绝对值
#  如果arr中没有，都要加入到arr里，但是只加一份
#  然后新的arr继续计算任何两个数差值的绝对值，
#  如果arr中没有，都要加入到arr里，但是只加一份
#  一直到arr大小固定，返回arr最终的长度
#  来自真实大厂笔试，没有在线测试，对数器验证

from math import gcd
from collections import Counter

class Solution:
    def len2(self, arr):
        max_val = 0
        g = 0

        # 找最大值 & 初始化gcd
        for num in arr:
            max_val = max(max_val, num)
            if num != 0:
                g = num

        # 全是0
        if g == 0:
            return len(arr)

        # 统计频率 + 计算整体gcd
        cnts = Counter(arr)
        for num in arr:
            if num != 0:
                g = gcd(g, num)

        # 核心计算
        ans = max_val // g

        max_cnt = 0
        for key, cnt in cnts.items():
            if key != 0:
                ans += cnt - 1
            max_cnt = max(max_cnt, cnt)

        # 处理0
        if 0 in cnts:
            ans += cnts[0]
        else:
            if max_cnt > 1:
                ans += 1

        return ans