# 状态转换：
# 我们将正数看作 $0$，负数看作 $1$。
# 子数组 $[i, j]$ 的乘积性质，可以通过前缀的异或和来判断。

# 计数原理：
# 如果当前前缀异或和为 cur，
# 那么之前出现过的相同异或和的状态（cnt[cur]）与当前位置组成的子数组，
# 其负数个数必为偶数（乘积为正）。
# 之前出现过的不同异或和的状态（cnt[cur ^ 1]）与当前位置组成的子数组，
# 其负数个数必为奇数（乘积为负）。


import sys

def solve():
    # 读取所有输入并切分为列表
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 为了逻辑清晰，我们直接处理剩下的数组元素
    arr = input_data[1:]
    
    # cnt[0]: 前缀中负数个数为偶数的次数
    # cnt[1]: 前缀中负数个数为奇数的次数
    # 初始状态：负数个数为0（偶数），所以 cnt[0] = 1
    cnt = [1, 0]
    
    ans_pos = 0  # 乘积为正的子数组数量 (ans1 in Java)
    ans_neg = 0  # 乘积为负的子数组数量 (ans2 in Java)
    
    cur = 0  # 当前前缀中负数的奇偶性状态
    
    for i in range(n):
        # 如果当前数字是负数，异或 1 切换状态；正数则状态不变 (异或 0)
        val = int(arr[i])
        if val < 0:
            cur ^= 1
        
        # 相同状态相减得偶数（正），不同状态相减得奇数（负）
        ans_pos += cnt[cur]
        ans_neg += cnt[cur ^ 1]
        
        # 记录当前状态
        cnt[cur] += 1
    
    # 题目要求先输出负数个数，再输出正数个数
    print(f"{ans_neg} {ans_pos}")

if __name__ == "__main__":
    solve()