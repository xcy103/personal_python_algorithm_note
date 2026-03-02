#矛盾 / 多解 / 唯一解 的高斯消元模板
#要详细区分矛盾和多解，就是要把不是作为主元（也就是自由元的行
#也要参与pk，找到最大的行与当前行进行交换
# 正确区分矛盾、多解、唯一解
# 0*x1 + 2*x2 = 3
# 0*x1 + 0*x2 = 0
# System.out.println("正确区分矛盾、多解、唯一解");
# mat[1][1] = 0; mat[1][2] = 2; mat[1][3] = 3;
# mat[2][1] = 0; mat[2][2] = 0; mat[2][3] = 0;
# gauss(2);
# print(2);
import sys

sml = 1e-7

def gauss(mat,n):
    for i in range(n):
        max_row = i
        for j in range(n):
            if j<i and abs(mat[j][j])>sml:
                continue
            if abs(mat[j][i])>abs(mat[max_row][i]):
                max_row = j
        mat[i],mat[max_row] = mat[max_row],mat[i]
        
        if abs(mat[i][i])>sml:
            pivot = mat[i][i]
            for j in range(i,n+1):
                mat[i][j]/=pivot
            for j in range(n):
                if j==i:
                    continue
                rate = mat[j][i]
                for k in range(i,n+1):
                    mat[j][k]-=rate*mat[i][k]

def main():
    data = list(map(float, sys.stdin.read().split()))
    n = int(data[0])
    idx = 1

    mat = [[0.0] * (n + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n + 1):
            mat[i][j] = data[idx]
            idx += 1
    gauss(mat,n)

    sign = 1
    for i in range(n):
        if abs(mat[i][i])<sml and abs(mat[i][n])>sml:
            sign = -1
            break
        if abs(mat[i][i])<sml:
            sign = 0
    
    if sign == 1:
        for i in range(n):
            print(f"x{i+1}={mat[i][n]:.2f}")
    else:
        print(sign)        

if __name__ == "__main__":
    main()