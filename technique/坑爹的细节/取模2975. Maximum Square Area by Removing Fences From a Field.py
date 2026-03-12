#他妈的不要提前对平方的面积取模
class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        MOD = 10**9 + 7
        
        h = [1] + h + [m]
        v = [1] + v + [n]
        
        h.sort()
        v.sort()

        hdis = set()
        
        for i in range(len(h)-1):
            for j in range(i+1,len(h)):
                hdis.add(h[j]-h[i])

        res = -1
        
        for i in range(len(v)-1):
            for j in range(i+1,len(v)):
                d = v[j]-v[i]
                if d in hdis:
                    res = max(res,d)

        return res*res % MOD if res != -1 else -1