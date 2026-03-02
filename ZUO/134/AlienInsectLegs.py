import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = max(n,m)

mat = [0]*(s+1)

for i in range(1,m+1):
    line = input().split()
    for j in range(n):
        if line[j]=='1':
            mat[i]|=1<<(j+1)
    
    x = int(input())
    if x:
        mat[i]|=1<<(s+1)

need = 0

def gauss(n):
    global need
    for i in range(1,n+1):
        pivot = -1
        for j in range(i,n+1):
            if mat[j]>>i&1:
                pivot = j
                break
        if pivot == -1:
            return
        if pivot!=i:
            mat[i],mat[pivot] = mat[pivot],mat[i]
        
        need = max(need,pivot)

        for j in range(1,n+1):
            if j!=i and mat[j]>>i&1:
                mat[j]^=mat[i]

gauss(s)

for i in range(1,n+1):
    if mat[j]>>i&1==0:
        print("Cannot Determine")
        sys.exit()

print(need)
for i in range(1,n+1):
    if (mat[i] >> (s + 1)) & 1:
        print("?y7M#")
    else:
        print("Earth")
