import sys

n,k = map(int,input().split())
if k>=n//2:
    print(1)
    print((n+1)//2)
    exit(0)

t = (n+2*k)//(2*k+1)
#可能刚好
if t*(2*k+1)==n:
    idx = []
    for i in range(k,n,2*k+1):
        idx.append(i+1)
    print(t)
    print(idx)
elif (2*k+1)*t-k<=n<=(2*k+1)*t-1:
    #恰好一次不够
    r = n-k-1
    idx = [n-(2*k+1)*(t-1)-k]
    for _ in range(t-1):
        idx.append(r+1)
        r-=2*k+1
    idx.sort()
    print(t)
    print(idx)
else:
    idx = []
    m = t-2
    for i in range(n):
        if n-(i+1)-k-(2*k+1)*(t-2)<2*k+1:
            for j in range(i,n,2*k+1):
                idx.append(j+1)
            break
    print(t)
    print(idx)


n, k = map(int, input().split())

mini = k + 1
maxi = 2 * k + 1

steps = (n - 1) // maxi + 1
print(steps)

f = n % maxi

if f == 0:
    cur = 1 + k
elif f <= mini:
    cur = 1
else:
    cur = 1 + f - mini

res = [cur]

for _ in range(steps - 1):
    cur += maxi
    res.append(cur)

print(*res)