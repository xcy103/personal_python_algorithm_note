#这几道题，递归的题，都好好看看，左的思路很不一样
#这里的思路是交换，可以自己画图理解一下，
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def f(i,nums):
            nonlocal ans
            if i==len(nums):
                ans.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                f(i+1,nums)
                nums[i],nums[j] = nums[j],nums[i]
        f(0,nums)
        return ans