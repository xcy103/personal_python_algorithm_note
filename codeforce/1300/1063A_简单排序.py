import sys

def solve():
    # 读入长度（虽然在 Python 中用不上，但需要读掉这行输入）
    n = sys.stdin.readline().strip()
    if not n:
        return
        
    # 读入字符串
    s = sys.stdin.readline().strip()
    
    # 直接对字符进行排序，相同字符会自动聚拢在一起
    ans = ''.join(sorted(s))
    
    print(ans)

if __name__ == '__main__':
    solve()