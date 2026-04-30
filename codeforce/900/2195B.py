import sys

def solve():
    # 使用快速读入
    input = sys.stdin.read().split()
    ptr = 0
    
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = [0] + [int(x) for x in input[ptr:ptr+n]]
        ptr += n
        
        # 并查集初始化
        parent = list(range(n + 1))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        # 根据规则连边：i 与 2i 连通
        for i in range(1, n // 2 + 1):
            union(i, 2 * i)
        
        # 判定：位置 i 的元素 a[i] 必须能通过交换到达位置 a[i]
        # 也就是说 i 和 a[i] 必须在同一个连通分量里
        possible = True
        for i in range(1, n + 1):
            if find(i) != find(a[i]):
                possible = False
                break
        
        results.append("YES" if possible else "NO")
    
    print('\n'.join(results))

if __name__ == "__main__":
    solve()