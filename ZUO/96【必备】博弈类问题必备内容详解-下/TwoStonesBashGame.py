#  两堆石头的巴什博弈
#  有两堆石头，数量分别为a、b
#  两个人轮流拿，每次可以选择其中一堆石头，拿1~m颗
#  拿到最后一颗石子的人获胜，根据a、b、m返回谁赢
# sg函数是干啥的，就是从0，开始，假设一次可以取1-m个石头
# 假设来到i，那么他就有m个前缀，分别是i-1，i-2...i-m，
# 就看这些前缀里，最小的没有出现过的自然数是什么，如果是0，那么sg[i]
# 这个状态就是必输的状态，如果不是0，就是必胜
import sys

# sg定理解法
def win2(a,b,m):
    n = max(a,b)
    sg = [0]*(n+1)
    for i in range(1,n+1):
        appear = [False] * (m + 1)

        for j in range(1,m+1):
            if i-j>=0:
                appear[sg[i-j]]==True

        for s in range(m+1):
            if not appear[s]:
                sg[i] = s
                break
    return "先手" if (sg[a] ^ sg[b]) != 0 else "后手"

# O(1)最优解
def win3(a, b, m):
    return "先手" if (a % (m + 1)) != (b % (m + 1)) else "后手"

# 示例
if __name__ == "__main__":
    a, b, m = 5, 7, 3
    print(win2(a, b, m))
    print(win3(a, b, m))