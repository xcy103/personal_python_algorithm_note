import sys

n,m = map(int,input().split())
s1 = list(input())
s2 = list(input())
f = 0
for ch in s1:
    if ch=='*':
        f = 1
        break

if f==0:
    l = 0
    r = 0
    if n!=m:
        print('NO')
        exit(0)
    while l<n and r<m:
        if s1[l]!=s2[r]:
            print('NO')
            exit(0)
        elif s1[l]==s2[r]:
            l+=1
            r+=1
    print('YES')
else:
    l = 0
    r = 0
    while l<n and r<m:
        if s1[l]=='*':break
        if s1[l]!=s2[r]:
            print('NO')
            exit(0)
        elif s1[l]==s2[r]:
            l+=1
            r+=1
    l+=1
    if n-l>m-r:
        print('NO')
        exit(0)
    p = n-1
    q = m-1
    while p>=l and q>=r:
        if s1[p]!=s2[q]:
            print('NO')
            exit(0)
        elif s1[p]==s2[q]:
            p-=1
            q-=1
    print('YES')


