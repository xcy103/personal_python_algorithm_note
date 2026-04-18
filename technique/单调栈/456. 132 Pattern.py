#这个真的特别巧，单调栈弹出的同时维护了最大的k值
class Solution:
    def find132pattern(self, nums):
        stack = []
        second = float('-inf')

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()

            stack.append(nums[i])

        return False