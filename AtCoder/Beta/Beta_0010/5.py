# 这道题意思是，你最多可以交换k次，相邻两个摊位会产生一个值
# 求所有相邻对(i和i+1,以及n和1）产生值的和最大值
# 数据量不大，可以直接暴力枚举每种排列
# 然后通过环计算这种排列产生的交换次数，因为数组是1-n的排列
# 打乱数的顺序会产生环，产生一个环就代表有一个交换的次数
# 然后求所有满足条件的排列，所产生值的和的最大值
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
