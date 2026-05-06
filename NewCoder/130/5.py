import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return
    n = len(s)
    arr = [ord(c) - ord('a') for c in s]
    
    final_ans = n
    
    # 枚举可能的步长 d
    for d in range(26):
        # dp[j] 表示当前人偶颜色为 j 时的最小修改次数
        # 初始状态：第一个人偶变更为颜色 j 的代价
        dp = [1] * 26
        dp[arr[0]] = 0
        
        for i in range(1, n):
            new_dp = [n] * 26
            target = arr[i]
            for j in range(26):
                # 如果当前位颜色定为 j，前一位只能是 p1 或 p2
                p1 = (j - d) % 26
                p2 = (j + d) % 26
                
                prev_min = dp[p1] if dp[p1] < dp[p2] else dp[p2]
                
                # 如果 j 等于原始颜色，代价不加；否则 +1
                new_dp[j] = prev_min + (0 if j == target else 1)
            dp = new_dp
            
        current_min = min(dp)
        if current_min < final_ans:
            final_ans = current_min
            
    print(final_ans)

solve()