import sys

MAXN = 37

mat = [[0]*(MAXN) for _ in range(MAXN)]
op = [0]*(MAXN)

n = 0
ans = 0

def prepare():
    global mat,op
    for i in range(1,n+1):
        for j in range(1,n+1):
            mat[i][j] = 0
        mat[i][i] = 1
        mat[i][n+1] = 1
        op[i] = 0

def swap(a, b):
    mat[a], mat[b] = mat[b], mat[a]

def gauss(n):
    #row
    for i in range(1,n+1):
        #col
        for j in range(1,n+1):
            if j<i and mat[j][j]==1:
                continue
            if mat[j][i]==1:
                swap(i,j)
                break
        
        if mat[i][i]==1:
            for j in range(1,n+1):
                if i!=j:
                    for k in range(i,n+2):
                        mat[j][k]^=mat[i][k]

def dfs(i,num):
    global ans
    if num>=ans:
        return 
    if i==0:
        ans = num
        return
    
    if mat[i][i]==0:
        op[i] = 0
        dfs(i-1,num)
        op[i] = 1
        dfs(i-1,num+1)
    
    else:
        cur = mat[i][n+1]
        for j in range(i+1,n+1):
            if mat[i][j]==1:
                cur^=mat[j][n+1]
        dfs(i-1,num+cur)

def main():
    global n, ans
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    n = data[idx]
    idx+=1

    prepare()

    m = data[idx]
    idx+=1

    for _ in range(m):
        u,v = data[idx], data[idx+1]
        idx+=2
        mat[u][v] = 1
        mat[v][u] = 1
    
    gauss(n)

    unique = True
    for i in range(1,n+1):
        if mat[i][i]==0:
            unique = False
            break
    
    if unique:
        ans = 0
        for i in range(1,n+1):
            if mat[i][n+1]:
                ans+=1
    else:
        ans = n
        dfs(n,0)
    
    print(ans)

if __name__ == "__main__":
    main()