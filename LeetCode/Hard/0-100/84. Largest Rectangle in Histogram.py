class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st = []
        n = len(h)
        left,right = [-1]*n,[n]*n

        for i,x in enumerate(h):
            while st and h[st[-1]]>=x:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
        
        ans = 0
        for x,l,r in zip(h,left,right):
            ans = max(ans,x*(r-l-1))
        return ans