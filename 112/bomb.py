
import sys

MAXN = 100001
bs = [0]*(MAXN<<2)
be = [0]*(MAXN<<2)

def up(i):
    bs[i] = bs[i << 1] + bs[i << 1 | 1]
    be[i] = be[i << 1] + be[i << 1 | 1]

# def build(l,r,i):
#     if l < r:
#         mid = (l + r) >> 1
#         build(l, mid, i << 1)
#         build(mid + 1, r, i << 1 | 1)
#     bs[i] = 0
#     be[i] = 0

def add(jobt, jobi, l, r, i):
    if l == r:
        if jobt == 0:
            bs[i] += 1
        else:
            be[i] += 1
    else:
        mid = (l + r) >> 1
        if jobi <= mid:
            add(jobt, jobi, l, mid, i << 1)
        else:
            add(jobt, jobi, mid + 1, r, i << 1 | 1)
        up(i)

def query(jobt, jobl, jobr, l, r, i):
    if jobl <= l and r <= jobr:
        return bs[i] if jobt==1 else be[i]
    
    mid = (l + r) >> 1
    ans = 0
    if jobl <= mid:
        ans += query(jobt, jobl, jobr, l, mid, i << 1)
    if jobr > mid:
        ans += query(jobt, jobl, jobr, mid + 1, r, i << 1 | 1)
    return ans

n,m = map(int,sys.stdin.readline().split())

out = []
for _ in range(m):
    jobl,jobr,op = map(int,sys.stdin.readline().split())
    if op == 1:
        # 记录新型地雷的起点和终点
        add(0, jobl, 1, n, 1)
        add(1, jobr, 1, n, 1)
    else:
        s = query(0, 1, jobr, 1, n, 1)
        e = 0 if jobl == 1 else query(1, 1, jobl - 1, 1, n, 1)
        out.append(str(s - e))

sys.stdout.write("\n".join(out) + "\n")
    