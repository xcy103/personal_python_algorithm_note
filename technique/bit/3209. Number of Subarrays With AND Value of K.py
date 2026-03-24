#https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/solutions/2833497/jian-ji-xie-fa-o1-kong-jian-pythonjavacg-u7fv/
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,x in enumerate(nums):
            for j in range(i-1,-1,-1):
                if nums[j]&x==nums[j]: break
                nums[j]&=x
            l = bisect_left(nums,k,0,i+1)
            r = bisect_right(nums,k,0,i+1)
            ans+=r-l
        return ans

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = right = 0
        for i, x in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if nums[j] & x == nums[j]:
                    break
                nums[j] &= x
            while left<=i and nums[left]<k: left+=1
            while right<=i and nums[right]<=k: right+=1
            ans += right - left
        return ans
#题目是and，一定是一个递增序列，后面的只会越来越小，如果倒着遍历发现等于了，就可以break了
