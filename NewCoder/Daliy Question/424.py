import sys

t = int(sys.stdin.readline().strip())

mod = 998244353
fac10 = [0]*(10**5+1)
fac10[0] = 1
for i in range(1,10**5+1):
    fac10[i] = fac10[i-1]*10%mod
res = []
for _ in range(t):
    a,b = sys.stdin.readline().split()

    sa = list(map(int,a))
    sa.reverse()
    for i in range(len(a)):
        sa[i] = sa[i]*fac10[i]%mod
    suma = sum(sa)
    sb = list(map(int,b))
    sb.reverse()
    tmp = 0
    for i in range(len(b)):
        tmp = (tmp + sb[i]*fac10[i]*len(a)%mod + suma)%mod
    
    res.append(str(tmp%mod))

print('\n'.join(res))

