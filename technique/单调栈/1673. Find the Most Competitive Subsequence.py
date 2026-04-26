class Solution:
    def mostCompetitive(self, nums, k):
        stack = []
        n = len(nums)
        
        for i, num in enumerate(nums):
            # 可以弹的条件
            while stack and stack[-1] > num and len(stack) + (n - i) > k:
                stack.pop()
            
            # 如果还没够k个，就加入
            if len(stack) < k:
                stack.append(num)
        
        return stack