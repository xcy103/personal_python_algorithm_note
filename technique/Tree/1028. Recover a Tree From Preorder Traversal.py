# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, s: str):
        i,n = 0,len(s)

        st = []

        while i < n:
            depth = 0
            
            while i < n and s[i]=='-':
                depth+=1
                i+=1
            
            val = 0
            while i<n and s[i].isdigit():
                val = 10*val + int(s[i])
                i+=1

            node = TreeNode(val)

            while len(st) > depth:
                st.pop()

            if st:
                p = st[-1]
                if p.left is None:
                    p.left = node
                else:
                    p.right = node
            
            st.append(node)
        return st[0]