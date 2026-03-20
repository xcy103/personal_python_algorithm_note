#多重背包 fastio 的pypy3写法
#这里用到的加速技巧，1，pypy3，手写max，min

import sys

def solve():
    # 使用 fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(map(int, input_data))
    n = next(it)
    w = next(it)
    
    # 拆分后的物品
    items = []
    for _ in range(n):
        l = next(it)
        c = next(it)
        k = 1
        while k <= c:
            items.append((k * l, k))
            c -= k
            k <<= 1
        if c > 0:
            items.append((c * l, c))

    inf = float('inf')
    dp = [inf] * (w + 1)
    dp[0] = 0
    
    # 核心循环优化
    for weight, count in items:
        if weight > w: continue # 剪枝
        
        # 这里的倒序循环是性能瓶颈
        for j in range(w, weight - 1, -1):
            prev = dp[j - weight]
            if prev != inf:
                new_val = prev + count
                if new_val < dp[j]:
                    dp[j] = new_val
                    
    ans = dp[w]
    print(ans if ans != inf else -1)

solve()