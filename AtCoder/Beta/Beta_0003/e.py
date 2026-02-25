# 状压dp，现在还是不太会

import sys

# 设置递归深度，尽管本解法为迭代式，但在某些混合解法中是好习惯
sys.setrecursionlimit(2000)

def solve():
    # 1. 高效读取输入
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        W = [int(next(iterator)) for _ in range(N)]
        C = [int(next(iterator)) for _ in range(M)]
    except StopIteration:
        return

    # 2. 预处理与剪枝
    
    # 如果所有包裹总重大于所有卡车总容量，直接返回 No (弱剪枝，非必须但有效)
    if sum(W) > sum(C):
        print("No")
        return

    # 关键贪心：将卡车容量从大到小排序
    # 优先使用大卡车能提高装载成功率
    C.sort(reverse=True)

    # 3. 预处理所有子集的重量
    # num_states = 2^N
    num_states = 1 << N
    w_sum = [0] * num_states
    
    # 使用位运算技巧高效计算子集和
    for i in range(N):
        bit = 1 << i
        weight = W[i]
        # 对于已经计算出的每个掩码，加上当前物品的重量形成新掩码
        for mask in range(bit):
            w_sum[bit | mask] = w_sum[mask] + weight

    # 4. 状态压缩 DP
    # dp[mask] = 装完 mask 集合的包裹所需的最少卡车数
    # 初始化为 M + 1 (代表不可达)
    dp = [M + 1] * num_states
    dp[0] = 0  # 没有包裹需要 0 辆车
    
    final_mask = num_states - 1
    
    # 遍历所有状态
    for mask in range(num_states):
        # 获取当前状态已使用的卡车数
        trucks_used = dp[mask]
        
        # 如果当前状态不可达，或者已经用完了所有卡车，则跳过
        if trucks_used >= M:
            continue
            
        # 当前即将使用的卡车容量
        current_capacity = C[trucks_used]
        
        # 计算剩余未装载的物品集合 (补集)
        remain = final_mask ^ mask
        
        # 强力剪枝：如果剩余的所有物品能一次性装入当前卡车，直接成功
        if w_sum[remain] <= current_capacity:
            print("Yes")
            return

        # 枚举子集技巧：遍历 remain 的所有子集 sub
        # 这是一个经典的位运算技巧：sub = (sub - 1) & remain
        sub = remain
        while sub > 0:
            # 如果子集 sub 能装入当前卡车
            if w_sum[sub] <= current_capacity:
                new_mask = mask | sub
                # 如果发现了更优或有效的路径，更新状态
                # 注意：由于我们按 mask 从小到大遍历，mask | sub 一定在 mask 后面被处理
                if dp[new_mask] > trucks_used + 1:
                    dp[new_mask] = trucks_used + 1
            
            #以此法递减枚举子集
            sub = (sub - 1) & remain

    # 5. 输出结果
    # 检查全集状态 (final_mask) 是否能在 M 辆车内完成
    if dp[final_mask] <= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()