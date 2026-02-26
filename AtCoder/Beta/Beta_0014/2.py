import sys

input = sys.stdin.readline

n, v = map(int, input().split())
d = list(map(int, input().split()))
t = list(map(int, input().split()))

prefix = 0
res = []

for i in range(n-1):
    prefix += d[i]  # 累计距离
    
    # checkpoint i+2
    # 判断 prefix < T_i * V
    if prefix < t[i] * v:
        res.append(i+2)

if not res:
    print(-1)
else:
    print(*res)