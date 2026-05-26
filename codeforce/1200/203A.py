# import sys

# x,t,a,b,m,n = map(int,input().split())

# arr1 = set()
# arr2 = set()
# for i in range(t):
#     arr1.add(max(a-m*i,0))
#     arr2.add(max(b-n*i,0))

# for num in arr1:
#     if x-num in arr2:
#         print('YES')
#         exit(0)
# print('NO')

#忽略了两道题都不做
import sys

x, t, a, b, m, n = map(int, input().split())

# 集合里先放入 0，代表这道题可以“不做”
arr1 = {0}
arr2 = {0}

# 遍历所有可能的提交时间 (0 到 t-1 分钟)
for i in range(t):
    arr1.add(a - m * i)
    arr2.add(b - n * i)

# 检查是否存在一种组合能恰好凑出 x 分
for num in arr1:
    if x-num in arr2:
        print('YES')
        exit(0)
print('NO')
