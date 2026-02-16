import sys

n,k,x = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
ret = None
if sum(arr[:k])<x:
    ret = -1
else:
    i = 0
    s = 0
    while s<x and i<k:
        s+=arr[i]
        i+=1
    j = 0
    while j<k and s>=x:
        s-=arr[j]
        j+=1
    ret = i+n-k-j
print(ret)
# 我的想法完全错了，我想的是，最坏情况首先如果最大的几个杯子里都是水
# 我们需要从最小的杯子里找水喝，所以我选了n-k个杯子，里面是水
# 然后我从最小的开始累加，如果累加过了就停止，返回我以为的答案，最差情况
# 我有的考虑是，不选最大的n-k个杯子，这个对了
# 但是最小还需要选几个杯子我没算对，你就剩下k个杯子了，你的酒都在里面
# 但是你没必要完全喝，而且不能从头算，因为从头算，你的杯子小，酒少
# 你就可能喝得多，错过了最佳答案，所以我们应该从头剔除可以不用管的杯子
# 因为他们的含量太少了，就算不喝这j个，剩下的k-j个杯子里的酒也够我们喝

import sys

def solve():
    # 读入 N, K, X
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, k, x = map(int, line1)
    
    line2 = sys.stdin.readline().split()
    arr = list(map(int, line2))

    # 从小到大排序
    arr.sort()
    
    # 所有酒的总量（最坏情况）：
    # 无论如何，酒至少是那最小的 K 个杯子之和。
    # 因为如果这 K 个最小的加起来都不够 X，那当酒正好是这 K 个时你就失败了。
    sake_min_total = sum(arr[:k])
    
    if sake_min_total < x:
        print("-1")
        return

    # 我们要选 m 个杯子。
    # 没选的杯子有 j = n - m 个。
    # 在这 j 个杯子中，最多能藏 min(k, j) 份酒。
    # 为了保证能喝到 X，必须满足：
    # (所有酒的总和) - (没选的杯子中，最大的那些酒的容量) >= X
    
    # 实际上，我们可以直接从最大的杯子开始选
    # 假设我们选了前 m 大的杯子
    # 那么没选的就是剩下的 n-m 个小的。
    # 即使那 n-m 个小杯子里全装了酒（最多装 k 个），
    # 只要 (所有酒的总量) - (剩下的里面最大的几个) >= X 即可。
    
    # 技巧：我们直接看排除掉多少个小杯子。
    # 假设我们从小到大排除 j 个杯子。
    # 剩下的杯子容量之和必须能覆盖“酒的总量中被藏起来的部分”。
    
    # 简单的做法：
    # 我们必须选最大的那些杯子。
    # 设我们选了 m 个最大的，没选的有 n-m 个最小的。
    # 即使那 n-m 个小的里装了酒，只要扣除掉它们，剩下的酒依然 >= X。
    
    # 实际上由于是“无论哪 K 个”，最坏情况就是酒在最小的 K 个里。
    # 而你选了 m 个杯子，最坏情况是那 K 个酒杯子中，有 min(K, n-m) 个你没选。
    # 为了喝到 X，你选的杯子必须包含足够多的“大杯子”来抵消损失。
    
    # 这里的逻辑等价于：
    # 找到最大的 m，使得从最小的 K 个酒里，剔除掉你没选的那部分，剩下的依然 >= X。
    
    current_sake_sum = sake_min_total
    # j 是我们不选的杯子数量 (从小到大)
    j = 0
    # 只要 j < k 且 剔除掉第 j 个（最小的酒）后依然满足条件，就可以不选这个杯子
    # 注意：如果你不选这个杯子，对手就会把酒放在这个杯子里。
    while j < k and current_sake_sum - arr[j] >= x:
        current_sake_sum -= arr[j]
        j += 1
    
    # 我们不选 j 个，所以要选 n - j 个
    print(n - j)

solve()