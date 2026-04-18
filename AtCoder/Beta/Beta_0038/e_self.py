import sys

N, M, K = map(int, input().split())
P = list(map(int, input().split()))
adj = [0]*N
for _ in range(K):
    u,v = map(int, input().split())
    u-=1
    v-=1
    adj[u] |= (1<<v)
    adj[v] |= (1<<u)

#分两半
n1 = N//2
n2 = N-n1
size1 = 1<<n1
size2 = 1<<n2
dp = [-1]*size1
dp[0] = 0

for mask in range(1,size1):
    lb = mask&-mask
    i = lb.bit_length() - 1
    prev = mask^lb

    if dp[prev] == -1:
        continue
    
    if adj[i]&prev:
        continue
    dp[mask] = dp[prev] + P[i]

for i in range(n1):
    bit = 1<<i
    s = 0
    while s<size1:
        s|=bit
        dp[s] = max(dp[s],dp[s^bit])
        s+=1

ans = 0
r_id = [i+n1 for i in range(n2)]

adj_left_mask = [0]*N
for i in range(N):
    adj_left_mask[i] = adj[i]&((1<<n1)-1)

for mask in range(size2):
    total = 0
    ok = True
    forbid = 0

    for i in range(n2):
        if (mask>>i)&1:
            u = r_id[i]
            #检查内部冲突。。其实这个还是不太懂
            #暴力检查这个mask的1是不是和之前的1有冲突
            for j in range(i):
                if (mask>>j)&1:
                    v = r_id[j]

                    if adj[u]>>v&1:
                        ok = False
                        break
            if not ok:
                break
            total = P[u]
            forbid |= adj_left_mask[u]
    if not ok:
        continue

    allow = ((1<<n1)-1)&(~forbid)

    best_left = dp[allow]
    if best_left!=-1:
        ans = max(ans,total+best_left)

print(min(ans, M))