# 核心难点与解法桥太长，石子太少：桥长达 $10^7$，直接开 DP 数组会内存溢出。
# 但石子只有 $100$ 个。

# 距离压缩原理：
# 当跳跃范围是 $[s, t]$ 时，如果两个石子之间的距离非常远，
# 超过了 $s$ 和 $t$ 的某个最小公倍数（或经验值 $t \times (t-1)$），
# 那么这段距离中间的某些部分是可以被“压缩”的，因为青蛙可以到达超长距离后的任何点。
# 特殊情况：当 $s = t$ 时，青蛙的落点是固定的，只需看石子坐标是否能被 $s$ 整除。


import sys

def solve():
    # 读入所有数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = int(input_data[1])
    t = int(input_data[2])
    m = int(input_data[3])
    
    # 石子位置
    stones_pos = sorted([int(x) for x in input_data[4:4+m]])
    
    # 情况 1: s == t
    # 只有当石子坐标是 s 的倍数时才会踩到
    if s == t:
        ans = sum(1 for x in stones_pos if x % s == 0)
        print(ans)
        return

    # 情况 2: s < t (路径压缩 DP)
    # 压缩距离的阈值：对于 s, t <= 10，2520 是 lcm(1..10)，
    # 但实际上根据数论结论，当距离 > t*(t-1) 以后都能到达，这里取 100 左右就足够安全。
    # 为了保险取 200。
    safe_dist = 200 
    
    compressed_pos = [0] * (m + 1)
    real_pos = [0] + stones_pos
    
    # 标记哪些位置有石子（在压缩后的空间内）
    # 最大的压缩空间长度：100个石子 * 200距离 + 安全距离
    max_l = m * safe_dist + safe_dist * 2
    has_stone = [False] * max_l
    
    curr_where = 0
    for i in range(1, m + 1):
        # 如果间距大于 safe_dist，则压缩为 safe_dist
        dist = real_pos[i] - real_pos[i-1]
        curr_where += min(dist, safe_dist)
        has_stone[curr_where] = True
    
    # 终点也需要平移压缩
    # 我们认为最后一颗石子跳过 safe_dist 距离就一定过河了
    target_len = curr_where + safe_dist
    
    # dp[i] 表示到达位置 i 踩到的最少石子数
    # 初始化为一个较大的数（石子总数 + 1）
    dp = [m + 1] * (target_len + 1)
    dp[0] = 0
    
    for i in range(1, target_len + 1):
        for j in range(s, t + 1):
            if i - j >= 0:
                # 状态转移：从 i-j 跳过来，如果 i 有石子则 +1
                cost = 1 if has_stone[i] else 0
                if dp[i-j] + cost < dp[i]:
                    dp[i] = dp[i-j] + cost
                    
    # 答案是所有超过最后一颗石子位置后的最小值
    print(min(dp[curr_where + 1 : target_len + 1]))

if __name__ == "__main__":
    solve()