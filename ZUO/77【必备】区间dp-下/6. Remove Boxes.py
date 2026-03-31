from typing import List
from itertools import groupby
from functools import cache
#  移除盒子
#  给出一些不同颜色的盒子boxes，盒子的颜色由不同的正数表示
#  你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止
#  每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1）
#  这样一轮之后你将得到 k * k 个积分
#  返回你能获得的最大积分总和
#  测试链接 : https://leetcode.com/problems/remove-boxes/
#  这种解法非常直观，比左得好理解，就是按照石头分组，分成tuple
#  每个tuple是颜色和这种颜色的长度，然后按照这个tuple来进行递归，
#  递归的过程中，如果遇到相同颜色的tuple，就把它们合并成一个tuple，
#  长度是两者之和，这样就可以得到更大的分数了
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        @cache
        def f(g):
            if not g:return 0

            (cl,ll),g = g[0],g[1:]

            res = ll*ll+f(g)

            for i,(cr,lr) in enumerate(g):
                if cr==cl:
                    res = max(res,f(g[:i])+f(((cl, ll+lr),) + g[i+1:]))
            return res
        bg = tuple((k, len(list(g))) for k,g in groupby(boxes))
        f.cache_clear()
        return f(bg)