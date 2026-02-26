# 模板题，分维度计算任意两点之间的距离
# 先排序，x2-x1 + x3-x2 + x3-x1
# 找规律，最后的公式是 x * (2*i - N + 1)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 读入所有城市
cities = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# 每一维独立处理
for k in range(M):
    arr = [cities[i][k] for i in range(N)]
    arr.sort()
    
    for i, x in enumerate(arr):
        ans += x * (2*i - N + 1)

print(ans)