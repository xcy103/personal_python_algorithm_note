import sys

n,m = map(int,sys.stdin.readline().split())
score = list(map(int,sys.stdin.readline().split()))
score = [0] + score
res = [0]*n
for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 0:
        res[i] = 0
        continue
    tmp = [(score[j],j) for j in arr[1:]]
    tmp.sort(key = lambda x:(-x[0],x[1]))
    res[i] = tmp[0][1]
print('\n'.join(map(str,res)))