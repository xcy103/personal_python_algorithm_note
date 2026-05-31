import sys

n = int(input())
arr = list(map(int,input().split()))

ans = 0
i = 0
while i<n:
    j = i+1
    while j<n and arr[j]-arr[j-1]==1:
        j+=1
    if j-i>1:
        if j==n:
            ans = max(ans,j-i-1)
        if j-i>3:
            ans = max(ans,j-i-2)
    i = j
print(ans)

import sys

n = int(input())
arr = list(map(int, input().split()))

# 按照题意，加上 a_0 = 0 和 a_{n+1} = 1001
# 注意：此时 arr 的下标变成了从 1 到 n
a = [0] + arr + [1001]

ans = 0

# 双重循环枚举所有可能的 i 和 j 对 (0 <= i < j <= n + 1)
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        # 核心判定公式
        if a[j] - j == a[i] - i:
            # 中间夹着的元素个数为 j - i - 1
            ans = max(ans, j - i - 1)

print(ans)