import sys
from collections import defaultdict
N,M = map(int,sys.stdin.readline().split())

op = 0
d = defaultdict(list)
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    if v in d[u]:
        op+=1
    else:
        d[v].append(u)
print(op)


# mat = [[0]*(N+1) for _ in range(N+1)]

# for _ in range(M):
#     u,v = map(int,sys.stdin.readline().split())
#     mat[u][v] = 1

# op = 0
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if mat[i][j] and mat[j][i]:
#             op+=1
# print(op//2)