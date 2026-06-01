import sys

from math import gcd
n,m = map(int,input().split())
times = list(map(int,input().split()))
gap = list(map(int,input().split()))
times.sort()
diff = []
c0 = 0
c1 = 0
for i in range(1,n):
    if times[i]%2==0:
        c0 = 1
    else:
        c1 = 1
    if times[i-1]%2==0:
        c0 = 1
    else:
        c1 = 1
    diff.append(times[i]-times[i-1])
s = diff[0]
for x in diff:
    s = gcd(s,x)
idx = -1
for i in range(m):
    if (s%gap[i])==0:
        if c0 and c1:
            #说明有奇数有偶数
            if gap[i]%2==0:
                continue
            else:
                idx = i
                break
        else:
            if c0:
                #只有偶数
                if gap[i]%2==0:
                    idx = i
                    break
            elif c1:
                #只有奇数
                if gap[i]%2==0:
                    idx = i
                    break
if idx==-1:
    print('NO')
    exit(0)
print('YES')
print(times[0],idx+1)

#想复杂了
import sys
input = sys.stdin.readline
from math import gcd

n, m = map(int, input().split())
x = list(map(int, input().split()))
p = list(map(int, input().split()))

g = 0
for i in range(1, n):
    g = gcd(g, x[i] - x[i-1])

for i in range(m):
    if g % p[i] == 0:
        print("YES")
        print(x[0], i+1)
        exit()

print("NO")