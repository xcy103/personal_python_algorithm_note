import sys

def solve():
    # 读入 n 和排列 a
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    # 转换为从 0 开始的索引，方便处理
    a = [x - 1 for x in a]
    
    vis = [False] * n
    belongs = [0] * n
    num_cycles = 0
    
    for i in range(n):
        if not vis[i]:
            curr = i
            while not vis[curr]:
                vis[curr] = True
                belongs[curr] = num_cycles
                curr = a[curr]
            num_cycles += 1
            
    base_swaps = n - num_cycles
    
    # 检查是否存在相邻位置在同一个环
    can_reduce = False
    for i in range(n - 1):
        if belongs[i] == belongs[i+1]:
            can_reduce = True
            break
            
    if can_reduce:
        print(base_swaps - 1)
    else:
        print(base_swaps + 1)

# 处理多组数据...
t = int(input())
for _ in range(t):
    solve()