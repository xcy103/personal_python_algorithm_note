# 核心逻辑摆放第 $i$ 个盘子时，为了保证不出现连续三个相同的菜品，我们只需考虑：
# 当前菜品与前一个不同：有 $(k-1)$ 种选法。
# 当前菜品与前一个相同：那么前一个必须与再前一个不同。

import sys

# 设置递归深度，防止深层递归崩溃
sys.setrecursionlimit(2000)

class PlateArrangement:
    MOD = 1000000007

    # --- 1. 记忆化搜索版本 ---
    def solve_memo(self, n, k):
        if n == 1: return k
        
        from functools import lru_cache

        @lru_cache(None)
        def f(i):
            if i == 0: return 1
            if i == 1: return k - 1
            # 状态转移：当前位置选与前一个不同的菜 (k-1) 种
            # 或者当前位置选与前一个相同的菜（要求前一个位置必须是“与更前一个不同”的情况）
            return ((f(i - 1) + f(i - 2)) * (k - 1)) % self.MOD

        # 最终结果：第 n 个盘子可以选 k 种，
        # 内部逻辑处理 n-1 和 n-2 的组合
        return ((f(n - 1) + f(n - 2)) * k) % self.MOD

    # --- 2. 迭代 DP 版本 (O(n)) ---
    def solve_dp(self, n, k):
        if n == 1: return k
        if n == 2: return k * k
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = k - 1
        for i in range(2, n):
            dp[i] = ((dp[i - 1] + dp[i - 2]) * (k - 1)) % self.MOD
            
        return ((dp[n - 1] + dp[n - 2]) * k) % self.MOD

    # --- 3. 矩阵快速幂版本 (O(log n)) ---
    # 适用于 n 非常大的情况
    def solve_matrix(self, n, k):
        if n == 1: return k
        s = k - 1
        # 初始矩阵 [f(0), f(1)] -> [1, s]
        start = [[1, s]]
        # 转移矩阵
        base = [[0, s], 
                [1, s]]
        
        def multiply(A, B):
            C = [[0, 0], [0, 0]]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for l in range(len(B)):
                        C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % self.MOD
            return C

        def power(A, p):
            res = [[1, 0], [0, 1]]
            while p > 0:
                if p & 1: res = multiply(res, A)
                A = multiply(A, A)
                p >>= 1
            return res

        final_matrix = multiply(start, power(base, n - 2))
        # res = (f(n-1) + f(n-2)) * k
        return ((final_matrix[0][0] + final_matrix[0][1]) * k) % self.MOD

# --- 测试 ---
sol = PlateArrangement()
n, k = 10, 3
print(f"n={n}, k={k}")
print("记忆化搜索结果:", sol.solve_memo(n, k))
print("迭代 DP 结果:   ", sol.solve_dp(n, k))
print("矩阵快速幂结果: ", sol.solve_matrix(n, k))