class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit -= root.val
        if root.left is None and root.right is None:  # root 是叶子
            # 如果 limit > 0 说明从根到叶子的路径和小于 limit，删除叶子，否则不删除
            return None if limit > 0 else root
        if root.left: root.left = self.sufficientSubset(root.left, limit)
        if root.right: root.right = self.sufficientSubset(root.right, limit)
        # 如果有儿子没被删除，就不删 root，否则删 root
        return root if root.left or root.right else None

