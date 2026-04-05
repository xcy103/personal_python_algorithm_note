import sys

data = sys.stdin.read().split()

T = int(data[0])
idx = 1
out = []
for _ in range(T):
    n = int(data[idx])
    idx+=1
    res = list(map(int,data[idx:idx+n]))
    idx+=n

    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans = max(ans,res[i]^res[j])
    out.append(str(ans))

print('\n'.join(out))