# 坐标三角形

class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        x1,y1 = p[0]
        x2,y2 = p[1]
        x3,y3 = p[2]
        return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))!=0
