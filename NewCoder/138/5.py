import sys

def solve():
    data = sys.stdin.read().split()

    if not data:
        return 
    
    T = int(data[0])
    idx = 1
    out = []

    INF = 10**18

    for _ in range(T):
        n = int(data[idx])
        idx+=1
        # 遍历当前测试用例的数字
        # 为了进一步省空间，这里可以直接在循环中处理，不显式切片创建大数组
        
        # mx[0] 维护偶数状态下 (dp[l-1] + a[l]) 的最大值
        # mx[1] 维护奇数状态下 (dp[l-1] + a[l]) 的最大值
        mx = [-INF,-INF]

        cur_dp = 0

        for _ in range(n):
            num = int(data[idx])
            idx+=1

            p = num%2

            nxt = cur_dp
            if mx[p]!=-INF:
                if num+mx[p]>nxt:
                    nxt = num+mx[p]
            if 