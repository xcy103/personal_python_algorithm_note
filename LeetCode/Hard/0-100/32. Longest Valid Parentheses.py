class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        st = [-1]
        ans = 0
        #栈里存“上一个不能匹配的位置”
        for i,ch in enumerate(s):
            if ch=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(ans,i-st[-1])
        return ans