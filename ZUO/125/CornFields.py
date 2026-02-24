import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)
MOD = 100000000

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

@lru_cache(None)
def f(i,j,s):
    if i==n:
        return 1
    if j==m:
        return f(i+1,0,s)
    # 选择不种
    # 把当前位置轮廓线状态清 0
    ans = f(i,j+1,s&~(1<<j))
    # 尝试种草
    # 条件：
    # 1. 当前格子可种
    # 2. 左边没种
    # 3. 上面没种
    if grid[i][j]==1 and \
       (j==0 or ((s>>(j-1)&1)==0)) and\
       ((s>>j&1)==0):
        ans = (ans + f(i,j+1,s|(1<<j)))%MOD
    return ans

print(f(0,0,0))