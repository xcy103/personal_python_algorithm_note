# 状态转换：
# 经典 DP：dp[i][j] 是前缀 $s1[i]$ 和 $s2[j]$ 的最长公共子序列长度。

# 优化 DP：dp[i][j] 表示 $s2$ 的前 $i$ 个字符中，
# 能够凑出长度为 $j$ 的公共子序列时，所需 $s1$ 的最小前缀长度。

def solve(s1,s2):
    n = len(s1)
    m = len(s2)
    
    NA = float('inf')
    # --- 1. 预处理 s1 的 next 数组 (序列自动机) ---
    # next_pos[i][c] 表示在 s1 的 i 位置之后，
    # 字符 c 第一次出现的位置

    next_pos = [[NA] * 26 for _ in range(n+1)]
    right = [NA]*26
    for i in range(n,-1,-1):
        for c in range(26):
            next_pos[i][c] = right[c]
        if i>0:
            right[ord(s1[i-1])-ord('a')] = i
    
    #i,j 表示 s2 的前 i 个字符中，
    # 提取长度为 j 的公共子序列，
    @__cached__
    def lcs2(i,j):
        if i<j:
            return NA
        if j==0:
            return 0
        
        cur = s2[i-1] - 'a'
        ans = lcs2(i-1,j)
        pre = lcs2(i-1,j-1)
        if pre!=NA:
            ans = max(ans,next[pre][cur])
        
        return ans

    ans = 0
    for j in range(m,0,-1):
        if lcs2(m,j)!=NA:
            ans = j
            break
    