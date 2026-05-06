import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_total = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            local_max = 0
            x1, y1 = points[i]
            
            for j in range(n):
                if j==i:continue
                x2, y2 = points[j]
                
                # 计算坐标差
                dx, dy = x2 - x1, y2 - y1
                
                # 计算斜率。这里使用 atan2 或者 将 dx, dy 除以最大公约数作为 key
                # Python 的 math.gcd 处理这种几何场景非常方便
                g = math.gcd(dx, dy)
                slope = (dx // g, dy // g)
                
                slopes[slope] += 1
                local_max = max(local_max, slopes[slope])
            
            # 结果要加上基准点 i 自身，所以是 local_max + 1
            max_total = max(max_total, local_max + 1)
            
        return max_total