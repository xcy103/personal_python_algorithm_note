# 博弈类问题大致分为，公平组合游戏、非公平组合游戏（绝大多数的棋类游戏）、反常游戏

# 只需要关注公平组合游戏（ICG），反常游戏是公平组合游戏的变形，经济类博弈也不是课程所讨论的范围
# 1，两个玩家轮流行动且游戏方式一致
# 2，两个玩家对状况完全了解
# 3，游戏一定会在有限步数内分出胜负
# 4，游戏以玩家无法行动结束

# 博弈的双方都被认为是神之个体，因为所有玩家对状况完全了解，且充分为自己打算，绝对理性
# 当局面确定，结果必然注定，并且没有任何随机的成分
# 游戏中的每一个状态，最终导致的结果也必然注定，只有必胜态、必败态，两种状态
# 这一类博弈问题的结果没有任何意外，一方可以通过努力去改变结果是不可能的，这一点是反直觉的

# 常用对数器打表来找规律，讲解042的内容

# 巴什博弈(Bash Game)
# 一共有n颗石子，两个人轮流拿，每次可以拿1~m颗石子
# 拿到最后一颗石子的人获胜，根据n、m返回谁赢

import random

# 动态规划进行所有尝试
# 为了验证
MAXN = 1001

dp = [[None] * MAXN for _ in range(MAXN)]


def bashGame1(n, m):
    if n == 0:
        return "后手"
    if dp[n][m] is not None:
        return dp[n][m]
    ans = "后手"
    for pick in range(1, m + 1):
        if n - pick >= 0 and bashGame1(n - pick, m) == "后手":
            # 后续过程的赢家是后续过程的后手
            # 那就表示此时的先手，通过这个后续过程，能赢
            ans = "先手"
            break
    dp[n][m] = ans
    return ans

#如果开始的石头数目是m+1的倍数，那么先手一定会让后手
#处于不是m+1的倍数的情况，也就是最后肯定是后手拿走几个石头
#相反如果开始的石头数目不是m+1的倍数，那么先手一定可以让
#后手处于是m+1的倍数的情况，也就是先手可以拿走最后一个石头
# 正式方法
def bashGame2(n, m):
    return "先手" if n % (m + 1) != 0 else "后手"


# 为了验证
if __name__ == "__main__":
    V = 500  # 需要比MAXN小
    testTimes = 5000
    print("测试开始")
    for _ in range(testTimes):
        n = random.randint(0, V - 1)
        m = random.randint(1, V)
        ans1 = bashGame1(n, m)
        ans2 = bashGame2(n, m)
        if ans1 != ans2:
            print("出错了!")
    print("测试结束")