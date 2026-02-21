# 考了一个小时，终于写出来了。
# 感觉这个题的难点在于如何计算一个排列的环数。
# 之前一直想用并查集来做，后来发现其实直接模拟就好了。
import sys
from math import permutations
n,k = map(int,sys.stdin.readline().split())

mat = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


def cnt(nums):
    vis = [False]*n
    c = 0
    for i in range(n): 
        if not vis[i]:
            c+=1
            j = i
            while not vis[j]:
                vis[j] = True
                j = nums[j]
    return n-c

def f(nums):
    res = 0
    for i in range(n):
        res+=mat[nums[i]][nums[(i+1)%n]]
    return res
ans = 0
for perm in permutations(range(n)):
    if cnt(perm)==k:
        ans = max(ans,f(perm))

print(ans)
