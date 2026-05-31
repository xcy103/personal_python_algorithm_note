import sys
#绷不住了，第一道1300的构造就写不出来

def solve():
    a, b, x = map(int, input().split())
    
    # 1. 构造跳变次数恰好为 x 的极简基底
    if x % 2 == 0:
        if a >= b:
            # 偶数次跳变，首尾相同，让 0 多消耗一点
            base = "01" * (x // 2) + "0"
            rem_0 = a - (x // 2 + 1)
            rem_1 = b - (x // 2)
        else:
            # 偶数次跳变，让 1 多消耗一点
            base = "10" * (x // 2) + "1"
            rem_0 = a - (x // 2)
            rem_1 = b - (x // 2 + 1)
    else:
        # 奇数次跳变，首尾不同
        if a >= b:
            base = "01" * ((x + 1) // 2)
            rem_0 = a - ((x + 1) // 2)
            rem_1 = b - ((x + 1) // 2)
        else:
            base = "10" * ((x + 1) // 2)
            rem_0 = a - ((x + 1) // 2)
            rem_1 = b - ((x + 1) // 2)
            
    # 2. 无损扩充：将剩余的 0 全部补在第一个 '0' 后面，剩余的 1 补在第一个 '1' 后面
    # 字符串的 replace(old, new, count) 方法正好可以只替换第一次出现的字符
    ans = base.replace('0', '0' + '0' * rem_0, 1)
    ans = ans.replace('1', '1' + '1' * rem_1, 1)
    
    print(ans)

if __name__ == '__main__':
    solve()