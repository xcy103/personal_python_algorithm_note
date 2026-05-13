import sys

n = int(input())
arr = list(map(int,input().split()))
tmp = []
for i,x in enumerate(arr):
    tmp.append((x,i))
tmp.sort()
k = (n+1)//2
if k%2==1:
    op1 = 0
    op2 = 0
    t1 = tmp[k//2][0]
    for i in range(k):
        op1+=abs(tmp[i][0]-t1)
    t2 = tmp[n-k//2-1][0]
    for i in range(1,k+1):
        op2+=abs(tmp[n-i][0]-t2)
    res = [0]*n
    
    if op1<op2:
        for i in range(k):
            res[tmp[i][1]] = t1
        for i in range(k+1,n):
            res[tmp[i][1]] = tmp[i][0]
    else:
        for i in range(1,k+1):
            res[tmp[n-i][1]] = t2
        for i in range(n-k):
            res[tmp[i][1]] = tmp[i][0]
    print(*res)
else:
    op1 = 0
    op2 = 0
    op3 = 0
    op4 = 0
    res = [0]*n
    t1 = tmp[k//2-1][0]
    t2 = tmp[k//2][0]
    for i in range(k):
        op1+=abs(tmp[i][0]-t1)
        op2+=abs(tmp[i][0]-t2)
        
    
    t3 = tmp[n-k//2][0]
    t4 = tmp[n-k//2-1][0]
    for i in range(1,k+1):
        op3+=abs(tmp[n-i][0]-t3)
        op4+=abs(tmp[n-i][0]-t4)
    mn = min(op1,op2,op3,op4)

    if op1==mn:
        for i in range(k):
            res[tmp[i][1]] = t1
        for i in range(k,n):
            res[tmp[i][1]] = tmp[i][0]
    elif op2==mn:
        for i in range(k):
            res[tmp[i][1]] = t2
        for i in range(k,n):
            res[tmp[i][1]] = tmp[i][0]
    elif op3==mn:
        for i in range(1,k+1):
            res[tmp[n-i][1]] = t3
        for i in range(n-k):
            res[tmp[i][1]] = tmp[i][0]
    elif op4==mn:
        for i in range(1,k+1):
            res[tmp[n-i][1]] = t4
        for i in range(n-k):
            res[tmp[i][1]] = tmp[i][0]
        
    print(*res)
    
    