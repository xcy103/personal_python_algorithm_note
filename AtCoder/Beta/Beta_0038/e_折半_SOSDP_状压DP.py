#题目意思是，选择一些点，权值和最大，不超过M，
#而且选择的点中，任意两点之间不直接相连
#有点像图上打家劫舍
#思想很想我昨天写的，BETA36的最后一题
#
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
P = list(map(int, input().split()))

adj = [0] * N
for _ in range(K):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u] |= (1 << v)
    adj[v] |= (1 << u)

# 分两半
n1 = N // 2
n2 = N - n1

# 左半：0 ~ n1-1
# 右半：n1 ~ N-1

# -------- 左半预处理 --------
size1 = 1 << n1
dp = [-1] * size1  # -1 表示非法

dp[0] = 0

for mask in range(1, size1):
    lb = mask & -mask
    i = (lb.bit_length() - 1)  # 第 i 位

    prev = mask ^ lb

    if dp[prev] == -1:
        continue

    # 检查冲突
    #这个就是看i的相邻点，和除去i之后的点有咩有重合
    #还好，能理解，就是为了判断我们现在在一半里选的
    #点是否是独立集，，错了，你这个只是dp["0"]!!!
    #是为了下面的SOSdp做准备
    if adj[i] & prev:
        continue

    dp[mask] = dp[prev] + P[i]

# SOS DP：子集最大值
# for i in range(n1):
#     for mask in range(size1):
#         if mask & (1 << i):
#             dp[mask] = max(dp[mask], dp[mask ^ (1 << i)])

for i in range(n1):
    bit = 1<<i
    s = 0
    while s<size1:
        s|=bit
        dp[s] = max(dp[s^bit],dp[s])
        s+=1

# -------- 右半枚举 --------
size2 = 1 << n2

ans = 0

# 预处理：右边节点映射到真实编号
right_id = [i + n1 for i in range(n2)]

# 提前把 adj 限制到左半
adj_left_mask = [0] * N
for i in range(N):
    adj_left_mask[i] = adj[i] & ((1 << n1) - 1)

for mask in range(size2):
    total = 0
    ok = True
    forbid = 0

    for i in range(n2):
        if (mask >> i) & 1:
            u = right_id[i]

            # 右半内部冲突
            for j in range(i):
                if (mask >> j) & 1:
                    v = right_id[j]
                    if (adj[u] >> v) & 1:
                        ok = False
                        break
            if not ok:
                break

            total += P[u]

            # 标记左边冲突
            #这一波我们选了U，所以另一半就不能选和U冲突的
            forbid |= adj_left_mask[u]

    if not ok:
        continue

    # 左边允许的mask
    allow = ((1 << n1) - 1) & (~forbid)

    best_left = dp[allow]

    if best_left != -1:
        ans = max(ans, total + best_left)

# 不超过 M
print(min(ans, M))

