# 状态定义：
# 由于数字范围高达 $10^9$，我们不能以数值为状态，但其二进制位最多只有 31 位。
# 因此，我们定义 pre[j] 表示：当前以二进制第 $j$ 位为 1 的数字结尾的最长合法子序列的长度。

# 转移方程：
# 对于每一个数字 num：遍历其所有为 1 的位（假设是第 $j$ 位），
# 找到这些位对应的 pre[j] 中的最大值。cur = max(pre[j]) + 1 
# 即为包含当前数字 num 能达到的最长长度。更新所有相关位：pre[j] = max(pre[j], cur)。


import sys

def solve():
    # 使用快读模式
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # pre[j] 记录第 j 位为 1 的最长子序列长度
    pre = [0] * 32
    
    # 依次处理每个数字
    for i in range(n):
        num = int(input_data[i + 1])
        
        # 1. 寻找当前数字能接在哪些序列后面
        # 只要 num 的第 j 位是 1，它就能接在任何以“第 j 位是 1 的数”结尾的序列后
        cur = 1
        for j in range(31):
            if (num >> j) & 1:
                if pre[j] + 1 > cur:
                    cur = pre[j] + 1
        
        # 2. 用当前找到的最长长度 cur，更新所有 num 中 bit 为 1 的位置
        for j in range(31):
            if (num >> j) & 1:
                if cur > pre[j]:
                    pre[j] = cur
                    
    # 最终结果是所有位中记录的最大值
    print(max(pre))

if __name__ == "__main__":
    solve()