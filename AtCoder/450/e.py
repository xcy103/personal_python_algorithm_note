import sys

def solve():
    x = sys.stdin.readline().strip()
    y = sys.stdin.readline().strip()
    q_str = sys.stdin.readline().strip()
    if not q_str: return
    q = int(q_str)

    # 1. 预处理长度和字符分布
    # max_n 取 90 左右即可覆盖 10^18
    MAX_K = 91
    lens = [0]*(MAX_K+1)
    # counts[k][char_idx] 存储 Sk 中字符的出现总数
    counts = [[0] * 26 for _ in range(MAX_K + 1)]
    lens[1] = len(x)
    lens[2] = len(y)
    for ch in x:
        counts[1][ord(ch)-ord('a')]+=1
    for ch in y:
        counts[2][ord(ch)-ord('a')]+=1
    INF = 10**18
    for i in range(3,MAX_K+1):
        lens[i] = lens[i-1] + lens[i-2]
        for j in range(26):
            counts[i][j] = counts[i-1][j] + counts[i-2][j]
    #定义递归查询函数
    def get_pre(k,n,ch_idx):
        if n<=0: return 0
        if k==1:
            tar = x[:min(n,lens[1])]
            return tar.count(chr(ord('a')+ch_idx))
        if k==2:
            tar = y[:min(n,lens[2])]
            return tar.count(chr(ord('a')+ch_idx))
        
        if n>=lens[k]:
            return counts[k][ch_idx]
        if n<=lens[k-1]:
            return get_pre(k-1,n,ch_idx)
        else:
            return counts[k-1][ch_idx] + get_pre(k-2,n-lens[k-1],ch_idx)
    res = []
    for _ in range(q):
        line = sys.stdin.readline().split()
        l, r, c = int(line[0]), int(line[1]), line[2]
        ch_idx = ord(c) - ord('a')
        ans = get_pre(MAX_K,r,ch_idx) - get_pre(MAX_K,l-1,ch_idx)
        res.append(str(ans))
    
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == '__main__':
    solve()