import sys
import random
#注意，不知要让右边界满足条件，还得让左边界也满足
n = int(input())
arr = list(map(int,input().split()))

res = [0]*n
for i in range(n//2):
    x = arr[i]
    if i==0:
        res[i] = 0
        res[n-i-1] = x
    else:
        res[i] = res[i-1]
        if x-res[i]>res[n-i]:
            res[n-i-1] = res[n-i]
            res[i] = x-res[n-i-1]
        else:
            res[n-i-1] = x-res[i]
print(*res) 


