#学一下怎么使用栈
import sys

# 提高读取速度
input = sys.stdin.read().split()

def solve():
    if not input: return
    ptr = 0
    t = int(input[ptr]); ptr += 1
    
    for _ in range(t):
        n = int(input[ptr]); ptr += 1
        if n == 0: continue
        
        # 1. 邻接表优化
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(input[ptr]); ptr += 1
            v = int(input[ptr]); ptr += 1
            g[u].append(v)
            g[v].append(u)
        
        res = [0] * (n + 1)
        
        # 2. 迭代 DFS 避免栈溢出和内存开销
        # stack 存储 (当前节点, 父节点, 是否为回溯阶段)
        stack = [(1, 0, False)]
        
        # 模拟 DFS 返回值：需要记录每个节点的 (tag, d)
        # 用数组模拟以节省内存
        tags = [False] * (n + 1)
        ds = [0] * (n + 1)

        while stack:
            u, f, visited = stack.pop()
            
            if not visited:
                # 第一次进入节点，标记为已访问并压回栈，准备回溯
                stack.append((u, f, True))
                # 邻居入栈
                for v in g[u]:
                    if v != f:
                        stack.append((v, u, False))
            else:
                # 回溯阶段：处理子节点逻辑
                if u != 1 and len(g[u]) == 1:
                    # 叶子节点
                    tags[u] = False
                    ds[u] = 0
                else:
                    curr_tag = True
                    curr_d = 0
                    for v in g[u]:
                        if v == f: continue
                        curr_tag &= tags[v]
                        curr_d += ds[v]
                    
                    if curr_tag:
                        res[u] = curr_d
                        tags[u] = False
                        ds[u] = curr_d
                    else:
                        res[u] = curr_d + 1
                        tags[u] = True
                        ds[u] = curr_d + 1

        print(*(res[1:]))

solve()