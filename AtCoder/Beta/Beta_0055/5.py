import sys
from collections import Counter
n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

left = arr[:n//2]
right = arr[n//2:]

def compute(nums):
    n = len(nums)
    #开始计算一半的数组能产生多少种和
    c = Counter()
    #怎么快速算出来，是不是相当于
    #一个位置有三种情况，不选，选1，选2
    def f(i,pre):
        nonlocal c
        if i==n:
            c[pre]+=1
            return
        f(i+1,pre)
        f(i+1,pre+nums[i][0])
        f(i+1,pre+nums[i][1])
    f(0,0)
    return c

c1 = compute(left)
c2 = compute(right)
res = 'No'
for v in c1.keys():
    if k-v in c2.keys():
        res = 'Yes'
        break
print(res)