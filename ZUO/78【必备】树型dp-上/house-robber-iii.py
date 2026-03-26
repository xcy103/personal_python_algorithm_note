#  没有上司的舞会
#  某大学有n个职员，编号为1...n
#  他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树
#  父结点就是子结点的直接上司
#  现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数 
#  但是如果某个职员的直接上司来参加舞会了
#  那么这个职员就无论如何也不肯来参加舞会了
#  所以请你编程计算邀请哪些职员可以使快乐指数最大
#  返回最大的快乐指数。
#  测试链接 : https://www.luogu.com.cn/problem/P1352
#  本题和讲解037的题目7类似
#  链式链接 : https://leetcode.com/problems/house-robber-iii/
class Solution:
    def rob(self, root):
        def f(node):
            if not node:
                return 0, 0
            
            ly, ln = f(node.left)
            ry, rn = f(node.right)
            
            # 偷当前
            rob = node.val + ln + rn
            
            # 不偷当前，我主要是这个状态错了，，不偷当前有很多可能可以选
            #左右节点可以偷或者不偷，然后取最大值i相加
            not_rob = max(ly, ln) + max(ry, rn)
            
            return rob, not_rob
        
        return max(f(root))