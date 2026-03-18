#非常经典的一道题，见过好多次，每次都想的是
#最大值小于下一个数字的时候排序
#有时候会让你找最小次数，有时候会让你找最小长度
#  最短无序连续子数组
#  给你一个整数数组nums，你需要找出一个 连续子数组
#  如果对这个子数组进行升序排序，那么整个数组都会变为升序排序
#  请你找出符合题意的最短子数组，并输出它的长度
#  测试链接 : https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/
def findUnsortedSubarray(nums):
    n = len(nums)
    
    # 从左往右：找 right
    #  max > 当前数，认为不达标
    #  从左往右遍历，记录最右不达标的位置
    right = -1
    max_val = float('-inf')
    for i in range(n):
        if max_val > nums[i]:
            right = i
        max_val = max(max_val, nums[i])
    
    # 从右往左：找 left
    #  min < 当前数，认为不达标
	#  从右往左遍历，记录最左不达标的位置
    left = n
    min_val = float('inf')
    for i in range(n - 1, -1, -1):
        if min_val < nums[i]:
            left = i
        min_val = min(min_val, nums[i])
    
    return max(0, right - left + 1)