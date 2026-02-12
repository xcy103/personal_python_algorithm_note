MAXN = 100001
LIMIT = 17

arr = [0] * MAXN
log2 = [0] * MAXN
bucket = [0] * MAXN
left = [0] * MAXN
right = [0] * MAXN
stmax = [[0] * LIMIT for _ in range(MAXN)]

def build(n):
    arr[0] = -23333333

    cnt = 0
    for i in range(1,n+1):
        if arr[i-1]!=arr[i]:
            right[cnt] = i-1
            cnt+=1
            left[cnt] = i
        bucket[i] = cnt
    right[cnt] = n

    log2[0] = -1
    for i in range(1,n+1):
        log2[i] = log2[i>>1] + 1
        stmax[i][0] = right[i] - left[i] + 1
    
    for p in range(1,log2[cnt]+1):
        h = 1<<(p-1)
        for i in range(1,cnt - (1<<p) + 2):
            stmax[i][p] = max(
                st[i][p-1],
                st[h+i][p-1]
            )

def query(l,r):
    if l>r:
        r,l = l,r
    
    lb = bucket[l]
    rb = bucket[r]

    if lb==rb:
        return r - l + 1
    a = right[lb] - l + 1
    b = r - left[rb] + 1

    if lb + 1 <= rb - 1:
        _from = lb + 1
        _to = rb - 1
        p = log2[_to - _from + 1]
        c = max(
            stmax[_from][p],
            stmax[_to - (1<<p) + 1][p]
        )
    return max(a,b,c)