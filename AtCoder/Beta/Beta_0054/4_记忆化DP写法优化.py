import sys

# 解除递归深度限制
sys.setrecursionlimit(5000)

n = int(input())
arr = list(map(int, input().split()))

# 不用列表，用单层字典进行记忆化
memo = {}

def f(l, r):
    # base case 1: 越界
    if l > r:
        return 0
    # base case 2: 只剩一张牌
    if l == r:
        return arr[l]
        
    # 用一个整数作为字典的 key，比元组 (l, r) 更快，且不用二维列表
    key = l * 3005 + r
    if key in memo:
        return memo[key]

    # 完全保留你原本的逻辑
    p1 = min(f(l + 2, r), f(l + 1, r - 1)) + arr[l]
    p2 = min(f(l + 1, r - 1), f(l, r - 2)) + arr[r]

    memo[key] = max(p1, p2)
    return memo[key]

a = f(0, n - 1)
print(a, sum(arr) - a)