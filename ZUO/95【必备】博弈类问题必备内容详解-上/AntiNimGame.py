# 反尼姆博弈(反常游戏)
# 一共有n堆石头，两人轮流进行游戏
# 在每个玩家的回合中，玩家需要选择任何一个非空的石头堆，并从这堆石头中移除任意正数的石头数量
# 谁先拿走最后的石头就失败，返回最终谁会获胜
# 先手获胜，打印John
# 后手获胜，打印Brother
# 测试链接 : https://www.luogu.com.cn/problem/P4279

import sys


def compute(stones):
    eor = 0
    cnt_one = 0
    n = len(stones)

    for x in stones:
        eor ^= x
        if x == 1:
            cnt_one += 1

    # 全是1的特殊情况
    if cnt_one == n:
        return "Brother" if n % 2 == 1 else "John"
    else:
        return "John" if eor != 0 else "Brother"


def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    res = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        stones = data[idx:idx + n]
        idx += n
        res.append(compute(stones))

    print("\n".join(res))


if __name__ == "__main__":
    main()