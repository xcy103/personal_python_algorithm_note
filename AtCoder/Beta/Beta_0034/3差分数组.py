# import sys
# n,k,t,c = list(map(int,sys.stdin.readline().split()))
# arr = list(map(int,sys.stdin.readline().split()))
# op = 0
# pre = 0
# nums = [0]*n
# for i in range(n):
#     if pre+arr[i]+nums[i]<t:
#         x = t-pre-arr[i]-nums[i]
#         pre+=nums[i]
#         op+=(x)*c
#         nums[i] = x
#         if i+k<n:
#             nums[i+k]-=x
#     pre+=nums[i]
        
# print(op)

import sys
n,k,t,c = list(map(int,sys.stdin.readline().split()))
arr = list(map(int,sys.stdin.readline().split()))
op = 0
pre = 0
nums = [0]*n
for i in range(n):
    pre+=nums[i]
    if pre+arr[i]<t:
        x = t-pre-arr[i]
        pre+=x
        op+=x*c
        if i+k<n:
            nums[i+k]-=x
        
print(op)


import sys

n, k, t, c = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

diff = [0] * (n + 1)  # 差分数组（多开一位更安全）
pre = 0               # 当前累计增量
ans = 0               # 总花费

for i in range(n):
    pre += diff[i]  # 更新当前位置的实际增量

    if arr[i] + pre < t:
        x = t - (arr[i] + pre)

        ans += x * c
        pre += x  
        if i+k<n:          # 当前立即生效
            diff[i + k] -= x    # k 之后失效

print(ans)