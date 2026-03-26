#  监控二叉树
#  给定一个二叉树，我们在树的节点上安装摄像头
#  节点上的每个摄影头都可以监视其父对象、自身及其直接子对象
#  计算监控树的所有节点所需的最小摄像头数量
#  测试链接 : https://leetcode.com/problems/binary-tree-cameras/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#空节点返回1，左右有一个孩子是2就是1，左右孩子有一个是0，就要2
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #主要就是三种状态
        ans = 0
        def f(node):
            nonlocal ans
            if not node:
                return 1
            
            l = f(node.left)
            r = f(node.right)
            if l==0 or r==0:
                ans+=1
                return 2
            elif l==1 and r==1:
                return 0
            else:
                return 1
        t = f(root)
        return ans + (1 if t==0 else 0)