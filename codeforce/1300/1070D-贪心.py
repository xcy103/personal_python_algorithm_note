import sys

n,k = map(int,input().split())
arr = list(map(int,input().split()))
op = 0
pre = 0
last = -1

        

print(op)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
pre = 0
for i in range(n):
    total = pre+arr[i]

    if total<k and pre>0:
        pre = 0
        ans+=1
    else:
        bag = total//k
        pre = total%k
        ans+=bag

if pre:
    ans+=1
print(ans)