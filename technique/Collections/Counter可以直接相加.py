from collections import Counter

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        c = c1 + c2

        for v in c.values():
            if v % 2:
                return -1

        ans = 0
        for k in c:
            target = c[k] // 2
            if c1[k] > target:
                ans += c1[k] - target

        return ans
