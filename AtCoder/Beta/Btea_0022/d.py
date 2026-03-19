#差分。。。差分前缀
import sys
n,k = map(int,sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
diff = [0]*(n+1)
cur = 0
op = 0
for i in range(n):
    cur+=diff[i]
    real = arr[i]^(cur%2)

    if real==1:
        if i+k>n:
            print(-1)
            exit()
        cur+=1
        diff[i+k]-=1
        op+=1
print(op)
    
