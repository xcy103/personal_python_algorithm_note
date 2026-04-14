class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low = list(map(int,list(str(low))))
        high = list(map(int,list(str(high))))
        n = len(high)
        diff = n - len(low)

        @cache
        def f(i,limit_low,limit_high,pre,num):
            if i==n:
                return 1 if num==0 and pre==0 else 0
            
            lo = low[i-diff] if limit_low and i>=diff else 0
            hi = high[i] if limit_high else 9
            ans = 0
            
            if limit_low and i<diff:
                ans += f(i+1,True,False,pre,num)
                lo = 1
            for d in range(lo,hi+1):
                nlimit_low = limit_low and d==lo and i>=diff
                nlimit_high = limit_high and d==hi
                npre = pre+(1 if d%2==0 else -1)
                nnum = (num*10+d)%k
                ans+=f(i+1,nlimit_low,nlimit_high,npre,nnum)

            return ans
        return f(0,True,True,0,0)