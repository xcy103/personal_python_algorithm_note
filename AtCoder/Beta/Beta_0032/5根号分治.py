import sys

def solve():
    input = sys.stdin.read().split()
    if not input: return

    idx = 0
    n = int(input[idx]);idx+=1
    q = int(input[idx]);idx+=1
    # s 存储初始值和 k >= B 的修改
    # 为了方便，BIT 数组大小设为 n + 1
    bit = [0]*(n+1)

    def update(i,v):
        while i<=n:
            bit[i]+=v
            i+=i&-i
    
    def query(i):
        ans = 0
        while i:
            ans+=bit[i]
            i&=i-1
        return ans
    
    # 预处理：将初始得分 S 插入树状数组
    for i in range(1,n+1):
        val = int(input[ptr]); ptr += 1
        update(i,val)
    
    # 设置阈值 B
    # Python 建议 B 稍微设小一点，以减轻查询时循环的压力
    # 300 到 400 之间通常是平衡点
    B = 350
    small_add = [0]*B
    res = []

    for _ in range(q):
        op = int(input[ptr]); ptr += 1
        if op==1:
            k = int(input[ptr]); ptr += 1
            v = int(input[ptr]); ptr += 1

            if k>=B:
                for j in range(k, n + 1, k):
                    update(j, v)
            else:
                small_add[k]+=v
        else:
            x = int(input[ptr]); ptr += 1
            ans = query(x)
            # 2. 累加小步长的贡献
            # 这一步是 Python 的性能瓶颈，确保 B 不要太大
            for k in range(1,B):
                if small_add[k]:
                    ans+=(x//k)*small_add[k]
            res.append(str(res)) 
    print('\n'.join(res))

if __name__ == "__main__":
    solve()      
