import sys

sml = 1e-7

def gauss(mat,n):
    for i in range(n):
        mar_row = i
        for j in range(n):
            if j<i and abs(mat[j][j])>=sml:
                continue
            if abs(mat[j][i])>abs(mat[mar_row][i]):
                mar_row = j
        mat[i],mat[mar_row] = mat[mar_row],mat[i]

        if abs(mat[i][i])>=sml:
            pivot = mat[i][i]
            for j in range(i,n+1):
                mat[i][j]/=pivot
            
            for j in range(n):
                if j==i:continue
                rate = mat[j][i]
                for k in range(i,n+1):
                    mat[j][k]-=rate*mat[i][k]

def main():
    data1 = list(map(float,sys.stdin.read().split()))
    n = int(data1[0])
    idx = 1
    data = [[0.0]*n for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n):
            data[i][j] = data1[idx]
            idx+=1
    
    mat = [[0.0]*(n+1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = 2*(data[i][j] - data[i+1][j])
            mat[i][n]+= (data[i][j]**2 - data[i+1][j]**2)
    
    gauss(mat,n)

    for i in range(n):
        print(f"{mat[i][n]:.3f}",end = " ")
    print()

if __name__ == "__main__":
    main()