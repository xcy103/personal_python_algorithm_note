# 唯一解好区分，就是流程走完后对角线上都是1

#高斯消元解决加法方程组模版(区分是否有唯一解)
#1. 如果表达式冗余，就是多给了一组方程，我们可以加一个自由元，加一列
#2. 主元确定的行，不一定能解出主元，主元可能被某些自由元影响
#3. 自由元不会被其他自由元影响，相互独立，不会影响
#4. 主元，自由元之间不会相互影响，主元会被自由元影响，自由元不会依赖主元
import sys

sml = 1e-7

def gauss(mat,n):
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(mat[j][i]) > abs(mat[max_row][i]):
                max_row = j

        mat[i], mat[max_row] = mat[max_row], mat[i]
        if abs(mat[i][i])<sml:
            return False
        
        pivot = mat[i][i]
        for j in range(i,n+1):
            mat[i][j]/=pivot
        
        for j in range(n):
            if j==i:
                continue
            rate = mat[j][i]
            for k in range(i,n+1):
                mat[j][k]-=rate*mat[i][k]
    return True

#形式为n*(n+1)
def Gauss(mat,n):
    for i in range(n):
        max_row = i
        for j in range(i+1,n):
            if abs(mat[j][i])>abs(mat[max_row][i]):
                max_row = j
        
        mat[i],mat[max_row] = mat[max_row],mat[i]
        if abs(mat[i][i])<sml:
            return False
        
        pivot = mat[i][i]
        for j in range(i,n+1):
            mat[i][j]/=pivot
        
        for j in range(n):
            if j==i: continue
            rate = mat[j][i]
            for k in range(i,n+1):
                mat[j][k]-=rate*mat[i][k]
    
    return True