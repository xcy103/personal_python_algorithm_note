import sys

def solve():
    # 使用 generator 快速读取所有输入，防止频繁调用 stdin.readline
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        # 读取接下来的 n 个数字作为 R 数组
        r = [int(x) for x in input_data[ptr : ptr + n]]
        ptr += n
        
        # L[i] 表示从左往右看，第 i 个位置为了满足约束能保留的最大行号（即最少操作）
        # 注意：向上移是数值变小，所以我们要计算的是“新的行号” x
        # 满足 x <= r[i] 且 x >= l[i-1] - 1 且 x <= l[i-1] + 1
        # 因为只能减小数值，所以限制条件是 x = min(r[i], l[i-1] + 1)
        
        l_bounds = [0] * n
        l_bounds[0] = r[0]
        for i in range(1, n):
            # 第 i 个位置的高度不能比左边高出超过 1
            l_bounds[i] = min(r[i], l_bounds[i-1] + 1)
            
        # R[i] 表示从右往左看，满足右侧约束的最大行号
        r_bounds = [0] * n
        r_bounds[n-1] = l_bounds[n-1] # 结合左侧的限制开始右侧扫描
        for i in range(n-2, -1, -1):
            # 第 i 个位置的高度不能比右边高出超过 1
            # 同时不能超过它自己在左扫时已经确定的上限
            r_bounds[i] = min(r[i], r_bounds[i+1] + 1)
            
        # 最终 R_i 就是满足双向约束的最小变动目标
        # 操作数 = 原始行号 - 最终行号
        ans = 0
        for i in range(n):
            ans += (r[i] - min(l_bounds[i], r_bounds[i]))
        results.append(str(ans))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()