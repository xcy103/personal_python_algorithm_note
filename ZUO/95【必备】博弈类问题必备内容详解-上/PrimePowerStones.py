# 质数次方版取石子(巴什博弈扩展)
# 一共有n颗石子，两个人轮流拿
# 每一轮当前选手可以拿 p的k次方 颗石子
# 当前选手可以随意决定p和k，但要保证p是质数、k是自然数
# 拿到最后一颗石子的人获胜
# 根据石子数返回谁赢
# 如果先手赢，返回"October wins!"
# 如果后手赢，输出"Roy wins!"
# 测试链接 : https://www.luogu.com.cn/problem/P4018
# 差不多跟平凡的巴氏博弈一个的规律，我们可以找到6的倍数不能表示为
# 任何质数的自然数幂次，就得到，如果开始ide石头是6的倍数，先手肯定会让
# 后手落入不是6倍数的情况，也就是最后几个石头一定可以被后手拿完
import sys


def compute(n):
    return "October wins!" if n % 6 != 0 else "Roy wins!"


def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    res = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        res.append(compute(n))
    print("\n".join(res))


if __name__ == "__main__":
    main()