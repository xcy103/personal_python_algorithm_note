import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    arr.append([a,b])

arr.sort(key = lambda x: -x[1])
cur = 0
res = 0
MOD = 10**9 + 7
for i in range(n):
    res = (res + arr[i][0] + arr[i][1]*cur)%MOD
    cur+=arr[i][0]
print(res)
# （1 <= n <= 10000）
#  a[i]，b[i]（1 <= a[i], b[i] <= 10000）


