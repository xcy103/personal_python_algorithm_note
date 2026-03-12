#  给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的组合
#  答案 不能 包含重复的组合。返回的答案中，组合可以按 任意顺序 排列
#  注意其实要求返回的不是子集，因为子集一定是不包含相同元素的，要返回的其实是不重复的组合
#  比如输入：nums = [1,2,2]
#  输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  测试链接 : https://leetcode.cn/problems/subsets-ii/
#  左这个思路有点抽象。。题目要求是返回所有子集，但是不能有重复
#  首先就是排序，这个可以想到，比如我们来到1了，后面2个数都是1，那我们肯定不可以每次只选一个1了
#  就是要每次选0，1，2，3这种方案，然后在来到1后面的数字，比如说3，继续去求
#  这里很巧的处理是，用了size，标记我放了多少个数字在path数组
#  要就是有效位，然后每次我们下标来到了终点，填入答案的时候
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = [0]*(len(nums))
        ans = []
        self.f(nums,0,path,0,ans)
        return ans
    
    def f(self,nums,i,path,size,ans):
        if i==len(nums):
            ans.append(path[:size])
            return
        
        j = i+1
        while j<len(nums) and nums[j]==nums[i]:
            j+=1
        self.f(nums,j,path,size,ans)
        while i<j:
            path[size] = nums[i]
            size+=1
            self.f(nums,j,path,size,ans)
            i+=1