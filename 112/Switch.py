import sys

MAXN = 100005
light = [0]*(MAXN<<2)
re = [False]*(MAXN<<2)

def up(i):
    light[i] = light[i << 1] + light[i << 1 | 1]

def lazy(i,n):
    light[i] = n - light[i]
    re[i] = 1^re[i]

def down(i,ln,rn):
    if re[i]:
        lazy(i << 1, ln)
        lazy(i << 1 | 1, rn)
        re[i] = False

def update(jobl, jobr, l, r, i):
    if jobl <= l and r <= jobr:
        lazy(i, r - l + 1)
        return
    mid = (l + r) >> 1
    # 下传标记，保证子节点数据正确
    down(i, mid - l + 1, r - mid)
    
    if jobl <= mid:
        update(jobl, jobr, l, mid, i << 1)
    if jobr > mid:
        update(jobl, jobr, mid + 1, r, i << 1 | 1)
    up(i)

def query(jobl, jobr, l, r, i):
    if jobl <= l and r <= jobr:
        return light[i]
    
    mid = (l + r) >> 1
    down(i, mid - l + 1, r - mid)
    ans = 0
    if jobl <= mid:
        ans += query(jobl, jobr, l, mid, i << 1)
    if jobr > mid:
        ans += query(jobl, jobr, mid + 1, r, i << 1 | 1)
    return ans

def solve():
    # 快速读入技巧：一次性读取所有输入并切分
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    ptr = 2
    output = []
    
    for _ in range(m):
        op = int(input_data[ptr])
        l = int(input_data[ptr+1])
        r = int(input_data[ptr+2])
        ptr += 3
        
        if op == 0:
            update(l, r, 1, n, 1)
        else:
            output.append(str(query(l, r, 1, n, 1)))
            
    # 一次性输出，比多次 print 快
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()