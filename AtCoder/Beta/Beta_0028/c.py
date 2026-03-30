import sys

data = sys.stdin.read().split()
n = int(data[0])
p = list(map(int,data[1:1+n]))
a = list(map(int,data[1+n:1+2*n]))
b = list(map(int,data[2*n+1:]))
s1 = sum(a)
s2 = sum(b)
ans = s1-s2
res = [0]*n
for i in range(n):
    res[i] = ans+p[i]-a[i]
print(max(res))