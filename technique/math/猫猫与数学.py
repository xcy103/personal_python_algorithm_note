import sys


def solve():
    # 读取输入
    line = sys.stdin.readline()
    if not line:
        return
    a, b = map(int, line.split())

    # 1. 处理 a == b 的特殊情况
    if a == b:
        if a > 1:
            print(0)
        else:
            print(1)
        return

    # 2. 计算差值 k
    k = abs(a - b)

    # 3. 如果差值为 1，根据辗转相除法性质，永远互质
    if k == 1:
        print(-1)
        return

    # 4. 找到 k 的所有质因子
    factors = []
    temp_k = k
    d = 2
    while d * d <= temp_k:
        if temp_k % d == 0:
            factors.append(d)
            while temp_k % d == 0:
                temp_k //= d
        d += 1
    if temp_k > 1:
        factors.append(temp_k)

    # 5. 遍历质因子，找最小的 c
    min_c = float("inf")
    for p in factors:
        remainder = a % p
        if remainder == 0:
            current_c = 0
        else:
            current_c = p - remainder

        if current_c < min_c:
            min_c = current_c

    print(min_c)


if __name__ == "__main__":
    solve()
