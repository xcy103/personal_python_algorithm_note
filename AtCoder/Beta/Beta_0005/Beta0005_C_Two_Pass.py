# LeetCode上也有一道题类似解法

import sys

# 增加递归深度并不是必须的，因为我们用的是迭代，但为了保险起见可以保留
sys.setrecursionlimit(200000)

def solve():
    # 使用快速IO读取所有输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    N = int(next(iterator))
    K = int(next(iterator))
    
    # 读取数组 A
    A = []
    for _ in range(N):
        A.append(int(next(iterator)))
    
    # 1. 从左向右扫描 (Left to Right Pass)
    # L[i] 表示满足自身高度和左侧所有约束后的最低高度
    L = [0] * N
    L[0] = A[0]
    for i in range(1, N):
        # 当前高度至少是 A[i]
        # 且不能比左边邻居低太多 (L[i-1] - K)
        L[i] = max(A[i], L[i-1] - K)
        
    # 2. 从右向左扫描 (Right to Left Pass)
    # R[i] 表示满足自身高度和右侧所有约束后的最低高度
    R = [0] * N
    R[N-1] = A[N-1]
    for i in range(N-2, -1, -1):
        # 当前高度至少是 A[i]
        # 且不能比右边邻居低太多 (R[i+1] - K)
        R[i] = max(A[i], R[i+1] - K)
        
    # 3. 计算最终结果
    total_added_flowers = 0
    for i in range(N):
        # 最终高度必须同时满足左右两边的约束
        final_height = max(L[i], R[i])
        total_added_flowers += (final_height - A[i])
        
    print(total_added_flowers)

if __name__ == "__main__":
    solve()