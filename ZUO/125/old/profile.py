import sys

# 增加递归深度，防止深搜爆栈
sys.setrecursionlimit(50000)

# 全局变量定义
MOD = 100000000
n = 0
m = 0
grid = []
dp = []

def get_val(s, j):
    """获取 s 的第 j 位"""
    return (s >> j) & 1

def set_val(s, j, v):
    """设置 s 的第 j 位为 v (0或1)"""
    if v == 0:
        return s & (~(1 << j))
    else:
        return s | (1 << j)

def f(i, j, s):
    """
    递归函数
    i: 当前行
    j: 当前列
    s: 轮廓线状态 (二进制压缩)
    """
    # 1. 基本结束条件：行越界，说明找到一种合法方案
    if i == n:
        return 1
    
    # 2. 列越界，换到下一行第 0 列
    if j == m:
        return f(i + 1, 0, s)
    
    # 3. 记忆化搜索：如果算过，直接返回
    if dp[i][j][s] != -1:
        return dp[i][j][s]
    
    # --- 核心转移 ---
    
    # 策略 1: 当前格子不种草 (set_val 把第 j 位重置为 0，表示当前行该位置空缺)
    ans = f(i, j + 1, set_val(s, j, 0))
    
    # 策略 2: 尝试种草
    # 必须满足三个条件：
    # a. 土地是适合种草的 (grid[i][j] == 1)
    # b. 左边没有草 (j==0 或者 s的第 j-1 位是 0)
    # c. 上边没有草 (s的第 j 位是 0 -> 注意：在更新前，s 的第 j 位存储的是上一行该列的状态)
    if grid[i][j] == 1 and \
       (j == 0 or get_val(s, j - 1) == 0) and \
       get_val(s, j) == 0:
        
        # 种草：将 s 的第 j 位设为 1，递归下一个格子
        ans = (ans + f(i, j + 1, set_val(s, j, 1))) % MOD
        
    # 记录结果
    dp[i][j][s] = ans
    return ans

def main():
    global n, m, grid, dp
    
    # 快速读取所有输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        # 初始化网格
        grid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                grid[i][j] = int(next(iterator))
        
        # 初始化 DP 表
        # 维度: [n][m][1 << m]
        # 注意：这里 1 << m 是状态总数
        maxs = 1 << m
        dp = [[[-1] * maxs for _ in range(m)] for _ in range(n)]
        
        # 开始计算
        print(f(0, 0, 0))
        
    except StopIteration:
        pass

if __name__ == "__main__":
    main()