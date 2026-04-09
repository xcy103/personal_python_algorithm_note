#差分数组＋贪心 错误的

# import sys
# from heapq import heappop,heappush
# n,m = list(map(int,sys.stdin.readline().split()))
# days = list(map(int,sys.stdin.readline().split()))
# books = list(map(int,sys.stdin.readline().split()))

# if sum(books)>sum(days):
#     print('No')
#     exit(0)
# h = []
# j = 0
# t = 0
# hb = []
# for i in range(n):
#     if len(h)<days[i]:
#         while j<m:
#             heappush(h,books[j])
#             j+=1
#     heappush(h,hb)
#     while h and h[0] == i+1:
#         heappop(h)
#         t+=1
#     while hb and hb[0]<=t:
#         heappop(hb)
#     if not hb:
#         print(False)
# if h:
#     print('No')
# else:
#     print('Yes')
""" 
PROBLEM: Library Inventory Check (Gale-Ryser Theorem Application)

[1. 核心矛盾]
- 每本书 j 需要检查 R[j] 次。
- 每一天 i 最多检查 L[i] 本不同的书。
- 约束：同一天内，同一本书不能被检查两次。

[2. 为什么你之前的思路 (Heap + Date Matching) 不对？]
- 误区 A：你把 R[j] 当成了“截止日期”。实际上 R[j] 是“总次数”，可以在任意日期分布。
- 误区 B：没有“消耗”过程。在模拟中，如果某天查了某本书，该书的剩余需求应减 1。
- 误区 C：效率问题。如果每天用堆弹出 L[i] 个元素再塞回去，复杂度 O(N * L * log M) 会超时。

[3. 正确的数学直觉：有效容量 (Effective Capacity)]
假设我们要检查需求量最大的 k 本书：
- 需求总量 = sum(R[0...k-1])  (R 已按降序排列)
- 供应总量 = 每一天能为这 k 本书提供的名额之和。

关键点：对于某一天 i，虽然它有 L[i] 个名额，但由于“每本书每天只能查一次”，
这一天对这 k 本书的贡献【最多只能是 k】。
所以，第 i 天的有效贡献 = min(k, L[i])。

[4. 判定公式]
对于每一个 k (1 <= k <= M):
    sum(R[0...k-1]) <= sum_{i=1 to N}( min(k, L[i]) )

[5. 视觉模型 (ASCII Art)]
把书的需求看作垂直的柱子，把天的容量看作水平的容器：

Books (R sorted desc):      Days (L sorted asc):
k=1: [R1]                   Day1: [L1] -> contrib min(k, L1)
k=2: [R1][R2]               Day2: [L2] -> contrib min(k, L2)
k=3: [R1][R2][R3]           ...

只要在任何一个 k 处，左边的总需求超过了右边的总有效容量，就输出 "No"。

[6. 算法复杂度]
- 排序 R: O(M log M)
- 排序 L: O(N log N)
- 遍历 k 并在 L 中二分找分界点: O(M log N)
- 总复杂度: O(M log M + N log N)，在 2s 内完美运行。
"""
import sys
from heapq import heappush, heappop

# 读入数据
line1 = sys.stdin.readline().split()
if not line1: exit()
n, m = map(int, line1)
days = list(map(int, sys.stdin.readline().split()))
books = list(map(int, sys.stdin.readline().split()))

# 1. 基础检查：单本书需求不能超过总天数
if max(books, default=0) > n:
    print('No')
    exit()

# 2. 这里的逻辑我们用刚才讨论的“判定式”，因为它是最稳健的
# 如果一定要用堆模拟每天的操作，代码会非常冗长且容易超时 (O(N * L_i * log M))
# 所以我们用排序+前缀和来实现你给出的那个“修正版”逻辑，但使用你的读入方式

books.sort(reverse=True)  # R 降序
days.sort()               # L 升序，方便二分

# 计算 L 的前缀和
pref = [0] * (n + 1)
for i in range(n):
    pref[i+1] = pref[i] + days[i]

import bisect

current_R_sum = 0
possible = True

# 核心判定
for k in range(1, m + 1):
    current_R_sum += books[k-1]
    
    # 找到有多少天的容量 L_i 是小于 k 的
    idx = bisect.bisect_left(days, k)
    
    # 理论最大容量：小于 k 的天贡献全部容量，大于等于 k 的天每天只能贡献 k
    max_cap = pref[idx] + (n - idx) * k
    
    if current_R_sum > max_cap:
        possible = False
        break

if possible:
    print('Yes')
else:
    print('No')

