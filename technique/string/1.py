from collections import defaultdict
s = "yexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzltyexodmnzlt"
n = len(s)
base = 499

pow_base = [1]*(n+1)
pre = [0]*n
pre[0] = ord(s[0]) - ord('a') + 1
for i in range(1,n+1):
    pow_base[i] = pow_base[i-1]*base
for i in range(1,n):
    pre[i] = pre[i-1]*base + ord(s[i]) - ord('a') + 1
def get_hash(l,r):
    ans = pre[r-1]
    if l>0:
        ans-=pre[l-1]*pow_base[r-l]
    return ans
k = (n)//2
d = defaultdict(int)
for l in range(1,k+1):
    for i in range(2*l-1,n):
        #s[i-2*l:i-l] s[i-l:i]
        p1 = get_hash(i-2*l+1,i-l+1)
        p2 = get_hash(i-l+1,i+1)
        if p1==p2:
            d[p1]+=1
print(len(d.keys()))