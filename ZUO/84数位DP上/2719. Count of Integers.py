#这个题非常经典，来自灵的数位dp模板
#补全低位和高位，然后用两个标记是否可以自由选择，标记上下界限

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        n = len(num2)
        high = list(map(int ,num2))
        low = list(map(int,num1.zfill(n)))

        @cache
        def dfs(i,cur,limit_low,limit_high):
            if cur>max_sum:
                return 0
            if i==n:
                return 1 if cur>=min_sum else 0
            
            hi = int(high[i]) if limit_high else 9
            lo = int(low[i]) if limit_low else 0

            res = 0
            for d in range(lo,hi+1):
                res = (res + dfs(i+1,cur + d, limit_low and d==lo,limit_high and d==hi))%MOD
            return res
        
        return dfs(0,0,True,True)