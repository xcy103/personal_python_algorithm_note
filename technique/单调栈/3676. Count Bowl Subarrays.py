# 这个也是单调栈加贡献
# 题解的思路是，来到一个元素，我们找他左边的第一个比他大的元素
# 我们维护一个单调递减栈，如果来到的元素比栈顶的元素大，就弹出
# 同时我们统计，如果弹出的元素下标比小于等于当前元素下标-2，说明构成
# 了一个合法子数组，
# 退出while循环之后，要么满足st空，要么满足栈顶元素大于等于当前元素
# 然后我们看看，如果栈顶元素下标小于等于当前元素下标-2，说明构成了一个合法子数组
class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left,right,st = [-1]*n,[n]*n,[]
        for i,x in enumerate(nums):
            while st and nums[st[-1]]<x:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
        op = 0
        for i in range(n):
            if left[i]!=-1 and right[i]!=n:
                op+=1
        return op
class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for i, x in enumerate(nums):
            while st and nums[st[-1]] < x:
                # j=st[-1] 右侧严格大于 nums[j] 的数的下标是 i
                if i - st.pop() > 1:  # 子数组的长度至少为 3
                    ans += 1
            # i 左侧大于等于 nums[i] 的数的下标是 st[-1]
            if st and i - st[-1] > 1:  # 子数组的长度至少为 3
                ans += 1
            st.append(i)
        return ans