import sys

n = int(sys.stdin.readline())
events = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    events.append((s, 1))   # start
    events.append((e, -1))  # end

# 关键：结束要排在开始前（因为 [s, e)）
events.sort()

cur = 0
ans = 0

for _, v in events:
    cur += v
    ans = max(ans, cur)

print(ans)