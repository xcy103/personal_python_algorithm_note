# import sys
# from functools import lru_cache
# sys.setrecursionlimit((1<<31)-1)
# n,k = list(map(int, sys.stdin.readline().split()))
# if n==1:
#     print(1)
#     exit(0)
# if k>(n+1)//2:
#     print(0)
#     exit(0)
# mod = 10**9+7
# #算法是没问题，就是复杂度太高了
# @lru_cache(None)
# def f(i,left):
#     if left==0:
#         return 1
#     if i==n:
#         return 0
#     if left>(n-i+1)//2:
#         return 0
#     ans = 0
#     for j in range(i,min(n,n+2-2*left)):
#         ans = (ans + f(j+2,left-1))%mod
#     return ans

# 不相邻选 K 个位置：

# x₁ < x₂ < ... < xₖ 且 xᵢ₊₁ ≥ xᵢ + 2

# 变换：yᵢ = xᵢ - (i-1)

# ⇒ 1 ≤ y₁ < y₂ < ... < yₖ ≤ N-K+1

# ⇒ 等价于从 N-K+1 个位置选 K 个

# 答案：C(N-K+1, K)

# 特判：K > (N+1)//2 → 0
import sys
input = sys.stdin.readline

mod = 10**9+7

n, k = map(int, input().split())

# 不可能情况
if k > (n + 1) // 2:
    print(0)
    exit()

# 预处理阶乘
maxn = n + 5
fac = [1] * maxn
for i in range(1, maxn):
    fac[i] = fac[i-1] * i % mod

# 快速幂
def qpow(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

# 组合数
def C(n, k):
    if k < 0 or k > n:
        return 0
    return fac[n] * qpow(fac[k], mod-2) % mod * qpow(fac[n-k], mod-2) % mod

print(C(n - k + 1, k))
