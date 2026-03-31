#  预测赢家
#  给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏
#  玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手
#  开始时，两个玩家的初始分值都是 0
#  每一回合，玩家从数组的任意一端取一个数字
#  取到的数字将会从数组中移除，数组长度减1
#  玩家选中的数字将会加到他的得分上
#  当数组中没有剩余数字可取时游戏结束
#  如果玩家 1 能成为赢家，返回 true
#  如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true
#  你可以假设每个玩家的玩法都会使他的分数最大化
#  测试链接 : https://leetcode.com/problems/predict-the-winner/

#这个题有点难想。。知道是区间dp了，状态定义是f(l,r)表示在区间l到r上先手能拿到的最大分数
#如果l==r，说明只有一个数了，先手只能拿这个数
#如果l+1==r，说明只有两个数了，先手只能拿较大的那个数
#如果l+1<r，说明有三个数了，先手可以拿左,或者右
#然后来到后手选，后手要选左或者右，使得接下来的函数返回值最小
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        @cache
        def f(l,r):
            if l==r:
                return nums[l]
            if l+1==r:
                return max(nums[l],nums[r])
            p1 = nums[l] + min(f(l+2,r),f(l+1,r-1))
            p2 = nums[r] + min(f(l+1,r-1),f(l,r-2))
            return max(p1,p2)
        ans = f(0,n-1)
        return ans*2 >= s