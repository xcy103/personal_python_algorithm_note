# 一来一回转为双倍起点

class Solution:
    def cherryPickup(self, g: List[List[int]]) -> int:
        n = len(g)

        @cache
        def f(a,b,c):
            d = a+b-c
            if a==n or b==n or c==n or d==n or g[a][b]==-1 or g[c][d]==-1:
                return -1
            
            if a==n-1 and b==n-1:
                return g[a][b]
            
            if a==c and b==d:
                num = g[a][b]
            else:
                num = g[a][b] + g[c][d]
            
            res = max(f(a+1,b,c+1),
                    f(a,b+1,c+1),
                    f(a,b+1,c),
                    f(a+1,b,c))
            
            ans = -1
            if res!=-1:
                ans = num+res
            return ans
        
        return max(0,f(0,0,0))
       