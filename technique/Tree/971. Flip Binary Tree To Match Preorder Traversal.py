#我错在了，交换顺序后不知道需要先便利右子树再左子树
class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        idx = 0

        def dfs(node):
            nonlocal idx
            if not node:
                return True

            # 当前节点必须匹配
            if node.val != voyage[idx]:
                return False
            idx += 1

            # 判断是否需要 flip
            if node.left and idx < len(voyage) and node.left.val != voyage[idx]:
                # flip
                res.append(node.val)
                # 先右后左
                return dfs(node.right) and dfs(node.left)
            else:
                # 正常顺序
                return dfs(node.left) and dfs(node.right)

        return res if dfs(root) else [-1]