from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:
            # 1️⃣ 更新高度（核心）
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # 2️⃣ 用你的单调栈函数
            ans = max(ans, self.largestRectangleArea(heights))

        return ans


    def largestRectangleArea(self, h: List[int]) -> int:
        st = []
        n = len(h)
        left, right = [-1] * n, [n] * n

        for i, x in enumerate(h):
            while st and h[st[-1]] >= x:
                right[st.pop()] = i
            if st:
                left[i] = st[-1]
            st.append(i)
        
        ans = 0
        for x, l, r in zip(h, left, right):
            ans = max(ans, x * (r - l - 1))
        return ans