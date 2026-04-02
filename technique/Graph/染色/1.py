import sys

# 增加递归深度防止 DFS 爆栈，或者改用 BFS
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.read().split()
    if not input: return
    
    ptr = 0
    T_cases = int(input[ptr])
    ptr += 1
    
    for _ in range(T_cases):
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr += 2
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input[ptr])
            v = int(input[ptr+1])
            k = int(input[ptr+2])
            ptr += 3
            # a_u - a_v = k  =>  a_u = a_v + k
            adj[v].append((u, k))
            adj[u].append((v, -k))
            
        a = [None] * (n + 1)
        possible = True
        
        for i in range(1, n + 1):
            if a[i] is None:
                # 开启新的连通分量 BFS
                stack = [i]
                a[i] = 10**12 # 初始给个大值，之后再平移
                component = [i]
                
                while stack:
                    u = stack.pop()
                    for v, k in adj[u]:
                        if a[v] is None:
                            a[v] = a[u] + k
                            stack.append(v)
                            component.append(v)
                        else:
                            if a[v] != a[u] + k:
                                possible = False
                                break
                    if not possible: break
                
                if not possible: break
                
                # 平移当前连通分量，确保所有 a_i >= 1
                min_val = min(a[node] for node in component)
                if min_val < 1:
                    diff = 1 - min_val
                    for node in component:
                        a[node] += diff
            if not possible: break
            
        if not possible:
            print("-1")
        else:
            print(*(a[1:]))

# solve()