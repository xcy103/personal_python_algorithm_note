import sys

N, M, Q, K = map(int, input().split())

books = []
for _ in range(M):
    s, d = map(int, input().split())
    books.append((d, s))  # 按 d 排

queries = []
for i in range(Q):
    l, r, t = map(int, input().split())
    queries.append((t, l, r, i))

# 排序（从大到小）
books.sort(reverse=True)
queries.sort(reverse=True)

# 树状数组
BIT = [0] * (N + 1)

def add(x):
    while x <= N:
        BIT[x] += 1
        x += x & -x

def query(x):
    s = 0
    while x > 0:
        s += BIT[x]
        x -= x & -x
    return s

def range_query(l, r):
    return query(r) - query(l - 1)

# 扫描
res = [0] * Q
p = 0

for t, l, r, idx in queries:
    while p < M and books[p][0] >= t:
        _, s = books[p]
        add(s)
        p += 1

    cnt = range_query(l, r)
    res[idx] = max(cnt - K, 0)

print('\n'.join(map(str, res)))