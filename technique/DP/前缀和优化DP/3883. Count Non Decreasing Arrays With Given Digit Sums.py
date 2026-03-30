#这是我能看懂的基础写法
MOD = 10**9+7
MX = 5001
MAX_DIGIT_SUM = 31  # 4999 的数位和最大
dig_sum = [0] * MX
for i in range(MX):
    dig_sum[i] = dig_sum[i//10] + i%10

class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        dp = [0]*MX
        for i in range(MX):
            if dig_sum[i]==digitSum[0]:
                dp[i] = 1
        
        for ds in digitSum[1:]:
            pre = [0]*MX
            pre[0] = dp[0]
            for i in range(1,MX):
                pre[i] = (pre[i-1]+dp[i])%MOD
            
            ndp = [0]*MX
            for x in range(MX):
                if dig_sum[x] == ds:
                    ndp[x] = pre[x]
            dp = ndp
        return sum(dp)%MOD
    
#现在要向神迹写法靠拢
MOD = 1_000_000_007
MX = 5001
MAX_DIGIT_SUM = 31  # 4999 的数位和最大
dig_sum = [0] * MX

# 预处理数位和
for x in range(MX):
    # 去掉 x 的个位，问题变成 x // 10 的数位和，即 dig_sum[x // 10]
    dig_sum[x] = dig_sum[x // 10] + x % 10

class Solution:
    def countArrays(self, digitSum: List[int]) -> int:
        s = [1] * MX  # f 的前缀和
        for ds in digitSum:
            if ds > MAX_DIGIT_SUM:
                return 0
            for x in range(MX):
                # 如果 dig_sum[x] != ds，那么 f[x] = 0，否则 f[x] = s[x]
                # 把 f[x] 的值填到 s[x] 中，那么只需要把 dig_sum[x] != ds 的 s[x] 置为 0
                if dig_sum[x] != ds:
                    s[x] = 0
                if x > 0:
                    s[x] = (s[x] + s[x - 1]) % MOD
        return s[-1]
    

# ==================================================
# 从普通DP → 神级写法 推导全过程
# ==================================================


# 【Step 0】当前写法（标准DP + 前缀和）
# --------------------------------------------------

# 定义：
# dp[x] = 以 x 结尾的方案数

# 代码结构：

# dp 初始化（第一轮）：

# dp = [0]*MX
# for x in range(MX):
#     if dig_sum[x] == digitSum[0]:
#         dp[x] = 1


# 每一轮：

# for ds in digitSum[1:]:
#     # 1. 前缀和
#     pre = [0]*MX
#     pre[0] = dp[0]
#     for i in range(1, MX):
#         pre[i] = (pre[i-1] + dp[i]) % MOD

#     # 2. 转移
#     ndp = [0]*MX
#     for x in range(MX):
#         if dig_sum[x] == ds:
#             ndp[x] = pre[x]

#     dp = ndp

# 答案：
# sum(dp)



# ==================================================
# 【Step 1】去掉 ndp（直接复用 dp）
# ==================================================

# 观察：

# ndp[x] = pre[x] (如果合法)

# → dp 完全被覆盖

# 所以可以直接写：

# for ds in digitSum[1:]:
#     pre = [0]*MX
#     pre[0] = dp[0]
#     for i in range(1, MX):
#         pre[i] = (pre[i-1] + dp[i]) % MOD

#     for x in range(MX):
#         if dig_sum[x] == ds:
#             dp[x] = pre[x]
#         else:
#             dp[x] = 0 # 不合法的直接置0，对的，这个没问题


# ==================================================
# 【Step 2】把 dp 改成“前缀含义”
# ==================================================

# 现在：

# dp[x] = 以 x 结尾

# 但我们每次都用：

# pre[x] = sum(dp[0..x])

# → 可以直接让 dp 存 prefix

# 定义改变：

# dp[x] = 结尾 <= x 的方案数


# 初始化：

# dp = [0]*MX
# for x in range(MX):
#     if dig_sum[x] == digitSum[0]:
#         dp[x] = 1

# # 转成前缀
# for i in range(1, MX):
#     dp[i] = (dp[i] + dp[i-1]) % MOD


# ==================================================
# 【Step 3】后续转移简化
# ==================================================

# 因为 dp 已经是 prefix：

# 原来：
# ndp[x] = sum(dp[0..x])

# 现在：
# 直接就是 dp[x]

# 所以：

# for ds in digitSum[1:]:
#     for x in range(MX):
#         if dig_sum[x] != ds:
#             dp[x] = 0

#     # 再做前缀
#     for i in range(1, MX):
#         dp[i] = (dp[i] + dp[i-1]) % MOD


# ==================================================
# 【Step 4】合并两层循环（关键一步）
# ==================================================

# 当前：

# 1. 先筛合法（置0）
# 2. 再做前缀和

# 观察：

# dp[i] = dp[i] + dp[i-1]

# 只依赖左边 → 可以一边扫一边做

# 合并：

# for ds in digitSum[1:]:
#     for x in range(MX):
#         if dig_sum[x] != ds:
#             dp[x] = 0
#         if x > 0:
#             dp[x] = (dp[x] + dp[x-1]) % MOD


# ==================================================
# 【Step 5】合并初始化（最终形态）
# ==================================================

# 原来需要单独处理第一轮：

# dp = [0]*MX
# if dig_sum[x] == digitSum[0]: dp[x]=1


# 可以改成：

# dp = [1]*MX

# 然后第一轮统一处理：

# for ds in digitSum:
#     for x in range(MX):
#         if dig_sum[x] != ds:
#             dp[x] = 0
#         if x > 0:
#             dp[x] = (dp[x] + dp[x-1]) % MOD


# ==================================================
# 【Final】神级写法
# ==================================================

# dp = [1]*MX

# for ds in digitSum:
#     for x in range(MX):
#         if dig_sum[x] != ds:
#             dp[x] = 0
#         if x > 0:
#             dp[x] = (dp[x] + dp[x-1]) % MOD

# return dp[MX-1]


# ==================================================
# 核心思想总结（必须记住）
# ==================================================

# 1. 原始转移：
#    dp[x] = sum(dp[0..x])

# 2. 优化手段：
#    → 前缀和

# 3. 关键升级：
#    → dp[x] 直接存 “<=x”

# 4. 终极优化：
#    → 前缀和原地计算
#    → 筛选 + 前缀合并

# ==================================================