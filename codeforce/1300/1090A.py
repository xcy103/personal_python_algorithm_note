import sys

n = int(input())

#存一个最大值和长度
arr = []
for _ in range(n):
    nums = list(map(int,input().split()))
    arr.append(nums)

#开始处理
nums = []
mx = 0
for x in arr:
    t = max(x[1:])
    mx = max(mx,t)
    nums.append([x[0],t])

op = 0
for l,num in nums:
    op+=(mx-num)*l
print(op)
