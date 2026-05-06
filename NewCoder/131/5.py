import sys

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    nums1 = arr[:]
    nums2 = arr[:]
    pre = [0]*n
    for i in range(1,n):
        pre[i]+=pre[i-1]+min(nums1[i],nums1[i-1])
        nums1[i]-=min(nums1[i],nums1[i-1])
    suf = [0]*n
    for j in range(n-2,-1,-1):
        suf[j]+=suf[j+1]+min(nums2[j],nums2[j+1])
        nums2[j]-=min(nums2[j],nums2[j+1])
    
    ans = 0
    if n==1:
        res.append(str(arr[0]))
        continue
    for i in range(n):
        if i==0:
            ans = max(ans,arr[i]+suf[i+1])
        elif i==n-1:
            ans = max(ans,arr[i]+pre[i-1])
        else:
            ans = max(ans,arr[i]+pre[i-1]+suf[i+1])
    
    res.append(str(ans))

print('\n'.join(res))