import sys

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
l = 0
r = 0
s = 0
for i in range(2*n):
    if i%2==0:
        #a操作
        if l<n and r<n:
            if a[l]>=b[r]:
                s+=a[l]
                l+=1
            else:
                r+=1
        elif r<n:
            r+=1
        elif l<n:
            s+=a[l]
            l+=1
    else:
        if l<n and r<n:
            if b[r]>=a[l]:
                s-=b[r]
                r+=1
            else:
                l+=1
        elif l<n:
            l+=1
        elif r<n:
            s-=b[r]
            r+=1
print(s)
