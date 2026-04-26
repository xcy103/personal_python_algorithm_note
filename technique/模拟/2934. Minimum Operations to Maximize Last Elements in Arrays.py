#不知道为什么会卡，要么交换要么不交换
#和之前0101交替一样
class Solution:
    def minOperations(self, nums1, nums2):
        n = len(nums1)

        def check(last1, last2):
            ops = 0
            for i in range(n - 1):
                a, b = nums1[i], nums2[i]

                # 不交换就合法
                if a <= last1 and b <= last2:
                    continue
                # 交换才合法
                elif b <= last1 and a <= last2:
                    ops += 1
                else:
                    return float('inf')
            return ops

        # 情况1：不交换最后一位
        ans1 = check(nums1[-1], nums2[-1])

        # 情况2：交换最后一位
        ans2 = check(nums2[-1], nums1[-1]) + 1

        res = min(ans1, ans2)
        return res if res != float('inf') else -1