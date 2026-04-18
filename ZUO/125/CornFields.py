#  种草的方法数(轮廓线dp+空间压缩)
#  给定一个n*m的二维网格grid
#  网格里只有0、1两种值，0表示该田地不能种草，1表示该田地可以种草
#  种草的时候，任何两个种了草的田地不能相邻，相邻包括上、下、左、右四个方向
#  你可以随意决定种多少草，只要不破坏上面的规则即可
#  返回种草的方法数，答案对100000000取模
#  1 <= n, m <= 12
#  测试链接 : https://www.luogu.com.cn/problem/P1879
import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)
MOD = 100000000

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#i,j 当前来到第i行第j列
#s 轮廓线状态，长度为m的二进制数，s
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