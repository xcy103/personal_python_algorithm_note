
import sys

def solve():
    #输入输出

    n = 1
    m = 1
    arr = list(range(n))

    sum1 = [0]*(n<<2)
    sum2 = [0]*(n<<2)
    addv = [0]*(n<<2)

    def up(i):
        sum1[i] = sum1[i<<1] + sum1[i<<1|1]
        sum2[i] = sum2[i<<1] + sum2[i<<1|1]
    
    def lazy(i,v,n):
        sum1[i] += v * n
        sum2[i] += sum1[i] * v * 2 + v * v * n
        addv[i] += v
    
    def down(i,ln,rn):
        if addv[i] != 0:
            lazy(i << 1, addv[i], ln)
            lazy(i << 1 | 1, addv[i], rn)
            addv[i] = 0.0
    
    def build(l,r,i):
        if l==r:
            sum1[i] = arr[l]
            sum2[i] = arr[l] * arr[l]
            return
        mid = (l + r) >> 1
        build(l, mid, i << 1)
        build(mid + 1, r, i << 1 | 1)
        up(i)

    def update(jobl, jobr, jobv, l, r, i):
        if jobl<=l and r<=jobr:
            lazy(i,jobv,r-l+1)
            return
        mid = (l + r) >> 1
        down(i, mid - l + 1, r - mid)
        if jobl <= mid:
            update(jobl, jobr, jobv, l, mid, i << 1)
        if jobr > mid:
            update(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
        up(i)
    
    def query(jobt,jobl, jobr, l, r, i):
        if jobl<=l and r<=jobr:
            return sum1[i] if jobt==2 else sum2[i]
        mid = (l + r) >> 1
        down(i, mid - l + 1, r - mid)
        res = 0.0
        if jobl <= mid:
            res += query(jobl, jobr, l, mid, i << 1)
        if jobr > mid:
            res += query(jobl, jobr, mid + 1, r, i << 1 | 1)
        return res

    build(1,n,1)
    results = []
    
    for _ in range(m):
        ops = list(map(int,sys.stdin.readline().split()))
        if len(ops)==4:
            jobl,jobr,jobv = ops[1],ops[2],ops[3]
            update(jobl,jobr,jobv,1,n,1)
        else:
            jobt,jobl,jobr = ops[0],ops[1],ops[2]
            size = jobr - jobl + 1
            if jobt==2:
                results.append(query(2,jobl,jobr,1,n,1))
            else:
                s1 = query(2,jobl,jobr,1,n,1)
                s2 = query(3,jobl,jobr,1,n,1)
                var = (s2 / size ) - (s1 / size) ** 2
                results.append(f"{var:.4f}")
    
    sys.stdout.write("\n".join(results)+"\n")

if __name__ == "__main__":
    solve()
