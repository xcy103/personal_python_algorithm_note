import sys

def solve():
    # 快速读取
    n = int(sys.stdin.read().strip())
    a_list = list(map(int,sys.stdin.read().split()))
    # if not input_data:
    #     return
    
    # n = int(input_data[0])
    # a_list = [int(x) for x in input_data[1:]]
    
    # 最大的 Ai 是 200,000
    max_a = max(a_list)
    
    # count[i] 表示长度恰好为 i 的 Bi 有多少个
    count = [0] * (max_a + 2)
    for a in a_list:
        count[a] += 1
        
    # 用差分/前缀和思想，计算每一位上有多少个 1
    # num_at_pos[i] 表示在从右往左数第 i 位上，有多少个 Bi 贡献了 1
    # 从最长的开始累加：长度为 10 的贡献了第 1~10 位，长度为 9 的贡献了 1~9 位
    num_at_pos = [0] * (max_a + 1)
    current_active = 0
    # 从高位向低位扫描统计覆盖数
    for i in range(max_a, 0, -1):
        current_active += count[i]
        num_at_pos[i] = current_active
        
    # 处理进位（从低位 i=1 开始）
    ans_digits = []
    carry = 0
    # num_at_pos 索引从 1 到 max_a
    for i in range(1, max_a + 1):
        current_sum = num_at_pos[i] + carry
        ans_digits.append(str(current_sum % 10))
        carry = current_sum // 10
        
    # 如果最后还有进位，继续处理
    while carry > 0:
        ans_digits.append(str(carry % 10))
        carry // 10
        
    # 翻转并输出（因为我们是从个位开始存的）
    sys.stdout.write("".join(ans_digits[::-1]) + "\n")

if __name__ == "__main__":
    solve()