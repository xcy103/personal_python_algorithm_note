#这道题竟然看不懂。。
# 其实很简单，就是绕圈
from collections import Counter
import sys
sys.setrecursionlimit(1000000)
import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
arr = [0]+arr
c = Counter(arr)
res = [0]*(n+1)
t = [0]*(n+1)
k = 1
def f(i):
    global t,k
    if t[i]!=0:
        if res[i]:
            return res[i]
        res[i]=k-t[i]
        return res[i]
    t[i] = k
    k+=1
    res[i] = f(arr[i])
    return res[i]

for i in range(1,n+1):
    if t[i]==0:
        f(i)

print(*res[1:])