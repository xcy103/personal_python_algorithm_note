#  超级洗衣机
#  假设有n台超级洗衣机放在同一排上
#  开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的
#  在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机
#  与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机
#  给定一个整数数组machines代表从左至右每台洗衣机中的衣物数量
#  请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数
#  如果不能使每台洗衣机中衣物的数量相等则返回-1
#  测试链接 : https://leetcode.cn/problems/super-washing-machines/

class Solution:
    def findMinMoves(self,arr):
        n = len(arr)
        total = sum(arr)

        if total % n != 0:
            return -1

        avg = total // n
        leftSum = 0
        ans = 0

        for i in range(n):
            # 左边需要多少件
            leftNeed = i * avg - leftSum
            # 右边需要多少件
            rightNeed = (n - i - 1) * avg - (total - leftSum - arr[i])

            if leftNeed > 0 and rightNeed > 0: #为什么需要单独讨论这个，是因为每一轮只能给一件衣服
                bottleneck = leftNeed + rightNeed
            else:
                bottleneck = max(abs(leftNeed), abs(rightNeed))

            ans = max(ans, bottleneck)

            leftSum += arr[i]

        return ans
        