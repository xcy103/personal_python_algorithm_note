#单调栈加贡献法，就是找左右边界

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left,right,st = [-1]*n,[n]*n,[]
        for i,x in enumerate(arr):
            while st and arr[st[-1]]>=x:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (i - l) * (r - i)  # 累加贡献
        return ans % (10 ** 9 + 7)