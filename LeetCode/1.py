from math import inf
from functools import cache
def minOperations(nums, k: int) -> int:
        if k==0:
            return 0
        if k>len(nums)//2:
            return -1
        n = len(nums)+2
        nums = [nums[-1]]+nums+[nums[0]]
        @cache
        def f(i,pre,left,t):
            if left==0:
                return 0
            if i==n-1:
                return inf
            if i==n-3:
                if left>1:
                    return inf
                return min(max(0,max(t[i-1],t[i+1])-t[i]+1),max(0,max(t[i],t[i+2])-t[i+1]+1))
            if i==n-2:
                if left>1:
                    return inf
                return max(0,max(t[i-1],t[i+1])-t[i]+1) if left==1 else 0
            ans = f(i+2,pre,left,t)
            if pre:
                c1 = f(i+2,1,left-1,t)+max(0,max(t[i-1],t[i+1])-t[i]+1)
                c2 = f(i+3,0,left-1,t)+max(0,max(t[i],t[i+2])-t[i+1]+1)
                return min(c1,c2,ans)
            else:
                return min(ans,f(i+2,0,left-1,t)+max(0,max(t[i-1],t[i+1])-t[i]+1))
        a1 = f(1,1,k,tuple(nums))
        f.cache_clear()
        a2 = f(2,0,k,tuple(nums))
        aa2 = min(a1,a2)
        #aa3 = ans if ans!=inf else -1
        #ans = min(aa1,aa2)
        return -1 if aa2==inf else aa2
minOperations([6,-7,11,13],2)
    
                        