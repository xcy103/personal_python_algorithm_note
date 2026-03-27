#  尼姆博弈(SG定理简单用法展示)
#  一共有 n 堆石头，两人轮流进行游戏
#  在每个玩家的回合中，玩家需要 选择任一 非空 石头堆，从中移除任意 非零 数量的石头
#  如果不能移除任意的石头，就输掉游戏
#  返回先手是否一定获胜
import sys

def nim2(arr):
    mx = max(arr)
    sg = [0]*(mx+1)

    for i in range(1,mx+1):
        appear = [False]*(mx+1)

        for j in range(i):
            appear[sg[j]] = True
        
        for s in range(mx+1):
            if not appear[s]:
                sg[i] = s
                break
    e = 0
    for num in arr:
        e^=sg[num]
    return "先手" if e != 0 else "后手"


# 示例
if __name__ == "__main__":
    arr = [3, 4, 5]
    print(nim2(arr))