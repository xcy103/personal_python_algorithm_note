class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        l = 0
        r = n-1
        pre_max = 0
        sur_max = 0
        ans = 0
        while l<r:
            pre_max = max(pre_max,h[l])
            sur_max = max(sur_max,h[r])
            if pre_max < sur_max:
                ans += pre_max - h[l]
                l+=1
            else:
                ans += sur_max - h[r]
                r-=1
        return ans

            
