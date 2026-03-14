#  球形空间的中心点
#  如果在n维空间中，那么表达一个点的位置，需要n个坐标的值
#  现在给定n+1个点，每个点都有n个坐标的值，代表在n维空间中的位置
#  假设这n+1个点都在n维空间的球面上，请返回球心的位置
#  球心的位置当然也是n个坐标的值，打印出来
#  在n维空间中，计算任意两点的距离，请用经典的欧式距离
#  1 <= n <= 10
#  坐标信息精确到小数点后6位，绝对值都不超过20000
#  测试链接 : https://www.luogu.com.cn/problem/P4035
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