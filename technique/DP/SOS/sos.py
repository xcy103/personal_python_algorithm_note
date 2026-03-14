import sys

t = int(sys.stdin.readline().strip())
res = []
while t:
    n,q = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    queries = list(map(int, sys.stdin.readline().split()))

    w = max(queries).bit_length()
    u = 1<<w
    f = [0]*u
    for i in range(1,min(n,u)+1):
        f[i] = arr[i-1]

    for i in range(w):
        bit = 1<<i
        s = 0
        while s<u:
            s|=bit
            f[s] += f[s^bit]
            s+=1
    
    for q in queries:
        res.append(f[q])
    t-=1

print('\n'.join(map(str, res)))