from collections import Counter
import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

# 枚举gcd
mx = max(arr)
ans = 0
c = Counter(arr)
for i in range(1,mx+1):
    tmp = 0
    for x in range(i,mx+1,i):
        tmp+=c[x]
    ans = max(ans,tmp*i)
print(ans)