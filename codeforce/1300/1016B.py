import sys
from itertools import accumulate

n, m, q = map(int, input().split())
a = list(input())
b = list(input())

que = []
for _ in range(q):
    l, r = map(int, input().split())
    que.append([l, r])


n,m = len(a),len(b)
#先求B的z数组
z=[0]*m
z[0] = m
r = c = 1
for i in range(1,m):
    t = 0 if r<=i else min(r-i,z[i-c])  
    while i+t<m and b[i+t]==b[t]:
        t+=1
    if i+t>r:
        c = i
        r = i+t
    z[i] = t
#然后再拿B的z数组去求A的e数组
e = [0]*n
c = r = 0
for i in range(n):
    t = 0 if r<=i else min(r-i,z[i-c])
    while i+t<n and t<m and a[i+t]==b[t]:
        t+=1
    if i+t>r:
        c = i
        r = i+t
    e[i] = t

# 然后就是查询个数
nums = [1 if x == m else 0 for x in e]
pre = [0] + list(accumulate(nums))
res = []

for l, r in que:
    # 转换为 0-indexed 的合法匹配起点区间：
    # 起点最左可以是 l - 1
    # 起点最右可以是 r - m
    limit_l = l - 1
    limit_r = r - m
    
    # 如果区间长度小于匹配串长度，说明不可能匹配成功，直接返回 0
    if limit_l > limit_r:
        res.append("0")
    else:
        # 利用前缀和计算 [limit_l, limit_r] 区间内 1 的个数
        res.append(str(pre[limit_r + 1] - pre[limit_l]))

print('\n'.join(res))