import bisect

def solve():
    # 1. 预处理 q > 2 的情况：n = p^(q-1)
    # 因为 2^(q-1) <= 2e9, q-1 最大约 30，所以 q 最大是 31
    special_nums = set()
    limit = 2 * 10**9
    
    # 简单筛出 45000 以内的素数，用于生成幂和辅助计数
    max_p = 44721 # sqrt(2e9)
    primes_small = []
    is_prime = [True] * (max_p + 1)
    for i in range(2, max_p + 1):
        if is_prime[i]:
            primes_small.append(i)
            for j in range(i*i, max_p + 1, i):
                is_prime[j] = False
                
    # 预处理所有的 q
    qs = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for q in qs:
        for p in primes_small:
            val = p**(q-1)
            if val > limit:
                break
            special_nums.add(val)
    
    sorted_special = sorted(list(special_nums))

    # 2. Lucy Hedgehog 算法：高效计算 pi(n)
    memo_pi = {}
    def count_primes(n):
        if n < 2: return 0
        if n in memo_pi: return memo_pi[n]
        
        # S[v] 表示在 [1, v] 中，去掉 [2, p] 的倍数后剩余的数字个数
        # 初始化时，假设除了 1 以外都是素数
        v_list = []
        i = 1
        while i <= n:
            v = n // i
            v_list.append(v)
            i = n // v + 1
        
        S = {v: v - 1 for v in v_list}
        
        # 动态规划优化
        for p in range(2, int(n**0.5) + 1):
            if S[p] > S[p-1]: # 说明 p 是素数
                sp_1 = S[p-1]
                p2 = p * p
                for v in v_list:
                    if v < p2: break
                    S[v] -= (S[v // p] - sp_1)
        
        memo_pi[n] = S[n]
        return S[n]

    # 3. 处理查询
    # 注意：T=10^4 时，如果每组都调用 Lucy 算法可能依然偏慢
    # 但在阿里/CF 等环境下，Lucy 算法的单次效率通常足以通过
    import sys
    input_data = sys.stdin.read().split()
    if not input_data: return
    T = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        l = int(input_data[idx])
        r = int(input_data[idx+1])
        idx += 2
        
        def get_total(x):
            if x <= 0: return 0
            # 隐式素数 = 素数个数 + 预处理的特殊幂个数
            c_primes = count_primes(x)
            c_special = bisect.bisect_right(sorted_special, x)
            return c_primes + c_special
        
        results.append(str(get_total(r) - get_total(l-1)))
    
    sys.stdout.write("\n".join(results) + "\n")

# solve()