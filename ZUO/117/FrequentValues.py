MAXN = 100001
LIMIT = 17

arr = [0] * MAXN
log2 = [0] * MAXN
bucket = [0] * MAXN
left = [0] * MAXN
right = [0] * MAXN
stmax = [[0] * LIMIT for _ in range(MAXN)]

def build(n):
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
    
    p = 1
    for p in range(1,LIMIT):
        for i in range(1,cnt - (1<<p) + 2):
            stmax[i][p] = max(
                stmax[i][p-1],
                stmax[i+(1<<(p-1))][p-1]
            )
    

def query(l,r):
    if l>r:
        l,r = r,l
    
    lb = bucket[l]
    rb = bucket[r]
    if lb==rb:
        return r-l+1

    a = right[lb] - l + 1
    b = r - left[rb] + 1
    c = 0
    if lb+1<rb:
        l = lb+1
        r=  rb-1
        l = r - l +1
        p = log2[l]
        c = max(stmax[lb+1][p], stmax[rb-(1<<p)+1][p])
    
    return max(a,b,c)

            