class Solution:
    def candy(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        l,r = [1]*n,[1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                l[i] = l[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                r[i] = r[i+1]+1
        
        for i in range(n):
            op+= max(l[i],r[i])
        return op