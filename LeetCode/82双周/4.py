class Solution:
    def validSubarraySize(self, nums: List[int], th: int) -> int:
        """
        题目意思：
        给你一个数组 nums 和一个整数 threshold
        
        要求：
        找一个子数组（连续），长度为 k，使得：
        
            子数组中每个元素 > threshold / k
        
        返回：
        👉 任意满足条件的子数组长度 k
        👉 如果不存在，返回 -1
        
        
        等价转化（关键）：
        
            nums[i] > threshold / k
        ⇔
            nums[i] * k > threshold
        
        👉 子数组中最小值 min * k > threshold
        
        
        核心思路（简述）：
        - 枚举“每个元素作为子数组最小值”
        - 求这个元素能扩展的最大区间长度 k
        - 判断 nums[i] * k > threshold
        
        
        如何求区间：
        - 对每个 nums[i]：
            left[i]  = 左边第一个 < nums[i] 的位置
            right[i] = 右边第一个 < nums[i] 的位置
        
        👉 区间长度：
            k = right[i] - left[i] - 1
        
        
        数据范围：
        - 1 <= n <= 1e5
        - 1 <= nums[i], threshold <= 1e9
        
        
        关键点：
        - 单调栈（求左右第一个更小元素）
        - 每个元素作为“最小值”只处理一次 → O(n)
        """

        n = len(nums)

        # left[i]：左边第一个 < nums[i] 的位置
        # right[i]：右边第一个 < nums[i] 的位置
        left, right, st = [-1] * n, [n] * n, []

        # 单调递增栈（求左右边界）
        for i, x in enumerate(nums):
            while st and nums[st[-1]] >= x:
                right[st.pop()] = i
            
            if st:
                left[i] = st[-1]
            
            st.append(i)

        # 枚举每个元素作为最小值
        for i in range(n):
            k = right[i] - left[i] - 1
            if nums[i] * k > th:
                return k

        return -1