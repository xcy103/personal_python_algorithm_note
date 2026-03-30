# 思维分析难度大，但是不用打表找规律
#  分裂游戏
#  一共有n个瓶子，编号为0 ~ n-1，第i瓶里装有nums[i]个糖豆，每个糖豆认为无差别
#  有两个玩家轮流取糖豆，每一轮的玩家必须选i、j、k三个编号，并且满足i < j <= k
#  当前玩家从i号瓶中拿出一颗糖豆，分裂成两颗糖豆，并且往j、k瓶子中各放入一颗，分裂的糖豆继续无差别
#  要求i号瓶一定要有糖豆，如果j == k，那么相当于从i号瓶中拿出一颗，向另一个瓶子放入了两颗
#  如果轮到某个玩家发现所有糖豆都在n-1号瓶里，导致无法行动，那么该玩家输掉比赛
#  先手希望知道，第一步如何行动可以保证自己获胜，要求返回字典序最小的行动
#  第一步从0号瓶拿出一颗糖豆，并且往2、3号瓶中各放入一颗，可以确保最终自己获胜
#  第一步从0号瓶拿出一颗糖豆，并且往11、13号瓶中各放入一颗，也可以确保自己获胜
#  本题要求每个瓶子的编号看做是一个字符的情况下，最小的字典序，所以返回"0 2 3"
#  如果先手怎么行动都无法获胜，返回"-1 -1 -1"
#  先手还希望知道自己有多少种第一步取糖的行动，可以确保自己获胜，返回方法数
#  测试链接 : https://www.luogu.com.cn/problem/P3185

# 把每一颗糖豆当作子游戏

import sys
input = sys.stdin.readline

MAXN = 21
MAXV = 101

nums = [0]*MAXN
sg = [0]*MAXN
appear = [False]*MAXV

def build():
    for i in range(1,MAXN):
        for x in range(MAXV):
            appear[x] = False
        for j in range(i-1,-1,-1):
            for k in range(j,-1,-1):
                appear[sg[j] ^ sg[k]] = True
        for s in range(MAXV):
            if not appear[s]:
                sg[i] = s
                break

def compute(n):
    e = 0
    for i in range(n-1,-1,-1):
        if nums[i]%2==1:
            e^=sg[i]
    if e==0:
        return "-1 -1 -1\n0"
    cnt = 0
    a = b = c = -1
    for i in range(n-1,0,-1):
        if nums[i]>0:
            for j in range(i-1,-1,-1):
                for k in range(j,-1,-1):
                    pos = e ^ sg[i] ^ sg[j] ^ sg[k]
                    if pos == 0:
                        cnt += 1
                        if a == -1:
                            a, b, c = i, j, k
    return f"{n - 1 - a} {n - 1 - b} {n - 1 - c}\n{cnt}"

# 预处理 SG
build()

t = int(input())
res = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        nums[n-i-1] = arr[i]
    res.append(compute())

print("\n".join(res))