import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    res = []

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        # ✅ 排序（替代 Counter）
        a.sort()

        # ✅ 统计频率（比 Counter 更快更稳）
        val = []
        cnt = 1
        for i in range(1, n):
            if a[i] == a[i-1]:
                cnt += 1
            else:
                val.append(cnt)
                cnt = 1
        val.append(cnt)

        # 不同元素个数
        op = len(val)

        # 贪心：优先删最小频率
        val.sort()

        s = 0
        for v in val:
            if s + v > k:
                break
            s += v
            op -= 1

        res.append(str(max(1, op)))

    print('\n'.join(res))

solve()