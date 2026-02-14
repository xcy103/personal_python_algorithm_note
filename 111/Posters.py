import sys

# 增加递归深度上限
sys.setrecursionlimit(200000)

def solve():
    # 使用快速读取所有数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr])
    m = int(input_data[ptr+1])
    ptr += 2
    
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = int(input_data[ptr])
        ptr += 1
    
    tree_sum = [0]*(n<<2)
    tree_max = [0]*(n<<2)

    def up(i):
        tree_sum[i] = tree_sum[i << 1] + tree_sum[i << 1 | 1]
        tree_max[i] = max(tree_max[i << 1], tree_max[i << 1 | 1])
    
    def build(l,r,i):
        if l == r:
            tree_sum[i] = tree_max[i] = arr[l]
            return
        mid = (l + r) >> 1
        build(l, mid, i << 1)
        build(mid + 1, r, i << 1 | 1)
        up(i)
    
    def query(jobl,jobr,l,r,i):
        if jobl <= l and r <= jobr:
            return tree_sum[i]
        mid = (l + r) >> 1
        ans = 0
        if jobl <= mid:
            ans += query(jobl, jobr, l, mid, i << 1)
        if jobr > mid:
            ans += query(jobl, jobr, mid + 1, r, i << 1 | 1)
        return ans

    def mod(jobl,jobr,jobv,l,r,i):
        if jobv > tree_max[i]:
            return
        if l == r:
            tree_sum[i] %= jobv
            tree_max[i] %= jobv
            return
        mid = (l + r) >> 1
        if jobl <= mid:
            mod(jobl, jobr, jobv, l, mid, i << 1)
        if jobr > mid:
            mod(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
        up(i)
    
    def update(jobi, jobv, l, r, i):
        if l == r:
            tree_sum[i] = tree_max[i] = jobv
            return
        mid = (l + r) >> 1
        if jobi <= mid:
            update(jobi, jobv, l, mid, i << 1)
        else:
            update(jobi, jobv, mid + 1, r, i << 1 | 1)
        up(i)

# 初始化线段树
    build(1, n, 1)
    
    results = []
    for _ in range(m):
        op = int(input_data[ptr])
        if op == 1:
            l = int(input_data[ptr+1])
            r = int(input_data[ptr+2])
            results.append(str(query(l, r, 1, n, 1)))
            ptr += 3
        elif op == 2:
            l = int(input_data[ptr+1])
            r = int(input_data[ptr+2])
            x = int(input_data[ptr+3])
            mod(l, r, x, 1, n, 1)
            ptr += 4
        else:
            k = int(input_data[ptr+1])
            x = int(input_data[ptr+2])
            update(k, x, 1, n, 1)
            ptr += 3
            
    # 输出结果
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()