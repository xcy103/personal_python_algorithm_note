import sys

t = int(input())


res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    st = []
    right = [n]*n
    left = [-1]*n
    
    for i,x in enumerate(arr):
        if st and arr[st[-1]]>=x:
            right[st.pop()] = i
        
        if st: left[i] = st[-1]
        st.append(i)
    log2 = [0]*(n+1)
    stmax = [[0]*16 for _ in range(n+1)]
    log2[0] = -1
    for i in range(1,n+1):
        log2[i] = log2[i>>1]+1
        stmax[i-1][0] = arr[i-1]
    
    for p in range(1,log2[n]+1):
        l = 1<<p
        h = 1<<(p-1)
        for i in range(n-l+1):
            stmax[i][p] = max(stmax[i][p-1],stmax[i+h][p-1])
    ans = -10**18
    for i in range(n):
        r = right[i] if right[i]<n else n-1
        l = left[i] if left[i]>=0 else 0
        p = log2[r-l+1]
        mx = max(stmax[l][p],stmax[r-(1<<p)+1][p])
        ans = max(ans,(mx-arr[i]+1)-(r-l+1))
    res.append(str(ans))

print('\n'.join(res))