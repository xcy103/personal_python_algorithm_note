# 斐波那契博弈(Fibonacci Game + Zeckendorf定理)
# 一共有n枚石子，两位玩家定了如下规则进行游戏：
# 先手后手轮流取石子，先手在第一轮可以取走任意的石子
# 接下来的每一轮当前的玩家最少要取走一个石子，最多取走上一次取的数量的2倍
# 玩家取走的数量必须不大于目前场上剩余的石子数量，双方都以最优策略取石子
# 根据规律先手一定会获胜，但是先手想知道
# 第一轮自己取走至少几颗石子就可以保证获胜了
# 测试链接 : https://www.luogu.com.cn/problem/P6487
# 首先是如果一个数是fib数字，如果先手不全部拿走，先手必输
# 然后一个数字，可以被拆成若干个不相邻的fib数字
import sys

MAXN = 10**15
MAXM = 101

f = [0] * MAXM
size = 0


def build():
    global size
    f[0] = 1
    f[1] = 2
    size = 1
    while f[size] <= MAXN:
        f[size + 1] = f[size] + f[size - 1]
        size += 1


def bs(n):
    l, r = 0, size
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if f[m] <= n:
            ans = f[m]
            l = m + 1
        else:
            r = m - 1
    return ans


def compute(n):
    ans = -1
    while n != 1 and n != 2:
        find = bs(n)
        if n == find:
            ans = find
            break
        else:
            n -= find
    if ans != -1:
        return ans
    else:
        return n


def main():
    build()
    data = sys.stdin.read().split()
    res = []
    for x in data:
        n = int(x)
        res.append(str(compute(n)))
    print("\n".join(res))


if __name__ == "__main__":
    main()