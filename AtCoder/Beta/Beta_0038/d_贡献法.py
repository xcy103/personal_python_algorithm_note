import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
mod = 998244353
s = sum(arr)%mod
#找出不合理的方案
total = s*pow(2,n-1,mod)%mod
fac = [1]*n
for i in range(1,n):
    fac[i] = fac[i-1]*i%mod
inv = [1]*n
inv[n-1] = pow(fac[n-1],mod-2,mod)
for i in range(n-2,-1,-1):
    inv[i] = inv[i+1]*(i+1)%mod

def comb(a,b):
    return fac[a]*inv[b]*inv[a-b]%mod
p = 0
for i in range(1,n//2+1):
    p = (p+s*comb(n-1,i-1)%mod)%mod
print((total-p+mod)%mod)
