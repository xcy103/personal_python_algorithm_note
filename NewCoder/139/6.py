import sys
from collections import deque
# 提高递归深度以防万一，虽然本代码采用迭代实现
sys.setrecursionlimit(300000)

def solve():
    # 使用快速读取提高性能
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [0] * (n + 1)
    in_degree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        target = int(input_data[i])
        a[i] = target
        in_degree[target] += 1
    
    MOD = 998244353
    ans = 1
    visited = [False] * (n + 1)
    
    # 1. 拓扑排序：处理所有非环上的节点（树枝）
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            
    # 改为更 Pythonic 的 while queue
    while q:
        u = q.popleft()  # 从左侧弹出，复杂度 O(1)
        visited[u] = True
        # 树枝上的点：只要不和它指向的点颜色相同即可，有 25 种选法
        ans = (ans * 25) % MOD
        
        v = a[u]
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)
            
    # 2. 遍历剩下的点，计算每个环的贡献
    for i in range(1, n + 1):
        if not visited[i]:
            # 发现一个新的环
            curr = i
            L = 0
            while not visited[curr]:
                visited[curr] = True
                curr = a[curr]
                L += 1
            
            # 环的染色公式: (k-1)^L + (-1)^L * (k-1)  其中 k = 26
            term1 = pow(25, L, MOD)
            if L % 2 == 0:
                ring_ways = (term1 + 25) % MOD
            else:
                ring_ways = (term1 - 25 + MOD) % MOD
            
            ans = (ans * ring_ways) % MOD
            
    print(ans)

if __name__ == "__main__":
    solve()