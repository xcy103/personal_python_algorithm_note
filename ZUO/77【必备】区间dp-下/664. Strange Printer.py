#  涂色 & 奇怪打印机
#  假设你有一条长度为5的木板，初始时没有涂过任何颜色
#  你希望把它的5个单位长度分别涂上红、绿、蓝、绿、红
#  用一个长度为5的字符串表示这个目标：RGBGR
#  每次你可以把一段连续的木板涂成一个给定的颜色，后涂的颜色覆盖先涂的颜色
#  例如第一次把木板涂成RRRRR
#  第二次涂成RGGGR
#  第三次涂成RGBGR，达到目标
#  返回尽量少的涂色次数
#  测试链接 : https://www.luogu.com.cn/problem/P4170
#  测试链接 : https://leetcode.com/problems/strange-printer/

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        s = list(s)

        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        
        for l in range(n-2,-1,-1):
            for r in range(l+1,n):
                p2 = p1 = 10**6
                #如果l==r，那么从l开始刷，可以解决掉r
                if s[l]==s[r]:
                    p1 = dp[l][r-1]
                else:
                    for k in range(l,r):
                        p2 = min(p2,dp[l][k]+dp[k+1][r])
                dp[l][r] = min(p1,p2)
        return dp[0][n-1]