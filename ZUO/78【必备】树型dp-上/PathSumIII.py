#  路径总和 III
#  给定一个二叉树的根节点 root ，和一个整数 targetSum
#  求该二叉树里节点值之和等于 targetSum 的 路径 的数目
#  路径 不需要从根节点开始，也不需要在叶子节点结束
#  但是路径方向必须是向下的（只能从父节点到子节点）
#  测试链接 : https://leetcode.com/problems/path-sum-iii/

#树上前缀和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        pre = defaultdict(int)
        pre[0] = 1
        ans = 0
        def dfs(node,cur_sum):
            nonlocal ans
            if not node:
                return

            cur_sum+=node.val
            ans+=pre[cur_sum-t]
            pre[cur_sum]+=1
            
            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)
            pre[cur_sum]-=1#这个很重要，可以画图理解，回去的时候需要修正前缀和
        dfs(root,0)
        return ans
