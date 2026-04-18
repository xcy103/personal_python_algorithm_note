import sys

def solve():
    # 读取输入并去掉两端的空白字符
    s = sys.stdin.readline().strip()
    if not s:
        return
    
    n = len(s)
    total_weight = 0
    
    # 遍历每一个可能的起点
    for i in range(n):
        f0 = 0  # 变成 0101... (偶数位与s[i]相同, 奇数位相反) 所需次数
        f1 = 0  # 变成 1010... (与f0相反) 所需次数
        
        # 从 i 开始向后扩展子串
        for j in range(i, n):
            # 目标字符：如果是 0101... 模式，当前位置 j 的字符应该是 (j-i) % 2
            # 我们只需要看 s[j] 是否符合该位置对应的期望字符
            
            # 期望模式 1: 0, 1, 0, 1... (相对于起始位置 i)
            expected_char_0 = str((j - i) % 2)
            if s[j] != expected_char_0:
                f0 += 1
            else:
                f1 += 1
            
            # 当前子串 s[i:j+1] 的权值是两种模式的最小值
            total_weight += min(f0, f1)
            
    print(total_weight)

if __name__ == "__main__":
    solve()