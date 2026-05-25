import sys


n,m = map(int,input().split())

if n<m:
    n,m = m,n

def ksm(a,p):
    ans = 1
    while p:
        if p&1: ans*=a
        p>>=1
        a*=a
    return ans
mn = 0
mx = 0
if m==1:
    if n==1:
        mn = 0
        mx = 8
    else:
        mn = ksm(10,n-1)-9
        mx = ksm(10,n)-1-1
else:
    if m==n:
        mn = 0
        mx = ksm(10,n)-1 - ksm(10,m-1)
    else:
        mn = ksm(10,n-1) - (ksm(10,m)-1)
        mx = ksm(10,n)-1 - ksm(10,m-1)
print(mn,mx)


