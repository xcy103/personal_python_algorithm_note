def f(val,l,r):
    if val==1:
        return r-l+1
    elif val==2:
        res = 0

        for id in range(26):
            cnt = pre[r][id] - pre[l - 1][id]
            res += cnt*(cnt-1)//2
        return res
    else:
        #(S_i-1 - S_l-1)*(S_r - S_i)
        le = r-l+1
        c1 = presu[r - 1] - presu[l] # - S_i*S_i-1
        c2,c3,c4 = 0,0,0
        for id in range(26):
            c4+=pre[l - 1][id] * pre[r][id]
            c3+=(double_pre[r-1][id]-double_pre[l][id])*pre[l-1][id]
            c2+=(double_pre[r-2][id]-double_pre[l-1][id])*pre[r][id]
        

n,q = map(int,input().split())

s = input()
pre = [[0]*26 for _ in range(n+1)]
presu = [0]*(n+1)
get = lambda s:ord(s)-97

for i,x in enumerate(s,1):
    for j in range(26):
        pre[i][j] = pre[i-1][j]
    idx = get(x)
    pre[i][idx]+=1

for i in range(1,n+1):
    presu[i] = presu[i - 1]
    tmp = 0
    for id in range(26):
        tmp+=pre[i][id]*pre[i-1][id]
    presu[i]+=tmp

double_pre = [[0 for _ in range(26)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for id in range(26):
        double_pre[i][id] = double_pre[i - 1][id] + pre[i][id]

