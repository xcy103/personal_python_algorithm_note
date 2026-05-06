mod = 10**9+7

n = int(input())

pw = pow(2, n-1, mod)

c = 1   # C(n,0)

for i in range(1, n+1):

    c = c * (n-i+1) % mod
    c = c * pow(i, mod-2, mod) % mod

    print(c * pw % mod, end=' ')