# 核心思路往返的本质：
# 青蛙去上学 $x$ 天，往返共计需要经过河流 $2x$ 次。

# 关键结论：如果青蛙的跳跃能力为 $y$，那么对于河中任意长度为 $y$ 的区间，
# 其内部所有石头的高度总和必须大于等于 $2x$。
# 原因：因为每次跳跃跨度不超过 $y$，所以任何长度为 $y$ 的“截面”都是青蛙无法直接跨过的。
# 要让 $2x$ 人次顺利通过这个截面，该区间内的总高度（容纳量）必须支撑 $2x$ 次踩踏。

# 算法实现：使用双指针（滑动窗口）维护一个区间，
# 使得该区间内的石头高度和恰好能支撑 $2x$ 次往返，此时窗口的宽度即为所需的最小跳跃能力。


import sys

def solve():
    # 使用读取全部输入的方式提高效率
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = int(input_data[1])
    
    # arr[0] 是起点 (位置0)
    # arr[1...n-1] 是石头高度
    # 位置 n 是学校，高度设为足够大（2 * x）
    arr = [0] * (n + 1)
    for i in range(1, n):
        arr[i] = int(input_data[i + 1])
    
    # 学校位置有无限高度（或者至少能撑过 2x 次）
    arr[n] = 2 * x
    
    ans = 0
    current_sum = 0
    r = 1
    
    # 目标值：总往返次数
    target = 2 * x
    
    # 滑动窗口 [l, r)
    for l in range(1, n + 1):
        # 只要当前窗口内的石头高度和不足以支撑 2x 次往返，就向右扩展窗口
        while r <= n and current_sum < target:
            current_sum += arr[r]
            r += 1
        
        # 此时窗口为 [l, r-1]，长度为 r - l
        ans = max(ans, r - l)
        
        # 左边界右移，减去移出窗口的石头高度
        current_sum -= arr[l]
        
    print(ans)

if __name__ == "__main__":
    solve()