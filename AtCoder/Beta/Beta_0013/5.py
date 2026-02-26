# 最大匹配问题
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))
    k = data[0]
    if k > 0:
        for x in data[1:]:
            graph[i].append(x-1)  # 员工编号改成0-index

match = [-1] * M  # 右边员工匹配到哪个时间段

def dfs(u, visited):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match[v] == -1 or dfs(match[v], visited):
                match[v] = u
                return True
    return False

ans = 0

for i in range(N):
    visited = [False] * M
    if dfs(i, visited):
        ans += 1

print(ans)