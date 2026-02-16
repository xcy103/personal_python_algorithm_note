import sys

# 提高读取效率
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    q = int(data[1])
    
    # 初始销售额 (1-indexed)
    s = [0] * (n + 1)
    # 树状数组
    bit = [0] * (n + 1)
    
    def update(i, delta):
        while i <= n:
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        res = 0
        while i > 0:
            res += bit[i]
            i&=(i-1)
        return res

    # 初始化：将初始销售额存入 BIT
    ptr = 2
    for i in range(1, n + 1):
        val = int(data[ptr])
        s[i] = val
        update(i, val)
        ptr += 1
        
    # 处理查询
    results = []
    for _ in range(q):
        t = int(data[ptr])
        if t == 1:
            l, r = int(data[ptr+1]), int(data[ptr+2])
            results.append(str(query(r) - query(l-1)))
            ptr += 3
        else:
            x, v = int(data[ptr+1]), int(data[ptr+2])
            # 注意：树状数组通常是增量更新，所以要算差值
            diff = v - s[x]
            update(x, diff)
            s[x] = v # 更新记录数组，以便下次算差值
            ptr += 3
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()