import sys
from collections import Counter

def solve():
    # 读取输入并处理可能的异常
    line = sys.stdin.read().split()
    if not line: return
    x, y = map(int, line)
    MOD = 10**9 + 7

    # 1. 快速质因数分解
    def get_factors(n):
        f = Counter()
        d = 2
        while d * d <= n:
            while n % d == 0:
                f[d] += 1
                n //= d
            d += 1
        if n > 1: f[n] += 1
        return f

    # 合并 x 和 y 的质因数
    counts = get_factors(x) + get_factors(y)
    
    # 2. 迭代生成所有因子并求和
    # factors 存储当前已生成的因子列表
    f = [1]
    for p,count in counts.items():
        nf = []
        for x in f:
            base = 1
            for _ in range(count+1):
                nf.append(base*f)
                base*=p
        f = nf

    # 3. 计算结果
    ans = sum(pow(d, d, MOD) for d in f) % MOD
    print(ans)

if __name__ == "__main__":
    solve()