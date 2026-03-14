# 2. 多个方程组成同余方程组
# a11*x1 + a12*x2 + ... + a1n*xn ≡ b1 (mod m)
# a21*x1 + a22*x2 + ... + a2n*xn ≡ b2 (mod m)
# ...
# am1*x1 + am2*x2 + ... + amn*xn ≡ bm (mod m)
#高斯消元法求同余方程组，就是来到这一行，
#如果元的系数不为0，就可以拿着这一行去消除其他行
#消除的方法是，最小公倍数，记得乘的时候要取模
import math
def gauss(mat,n,MOD):
    """
    mat : 二维列表，下标从1开始使用
          mat[i][1..n] 为系数
          mat[i][n+1] 为常数项
    n   : 变量个数
    MOD : 质数模数
    处理后 mat 会变为行最简形式（保留多解结构）
    """

    inv = [0]*MOD
    inv[1] = 1
    for i in range(2,MOD):
        inv[i] = (MOD - inv[MOD%i]*(MOD//i)%MOD)%MOD
        
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<i and mat[j][j]!=0:
                continue
            if mat[j][i]!=0:
                mat[i],mat[j] = mat[j],mat[i]
                break
        
        if mat[i][i]!=0:
            for j in range(1,n+1):
                if i!=j and mat[j][i]!=0:
                    g = math.gcd(mat[j][i],mat[i][i])
                    a = mat[i][i]//g
                    b = mat[j][i]//g

                    # 若 j 行已有主元，需要维护之前的关系
                    if j<i and mat[j][j]!=0:
                        for k in range(j,i):
                            mat[j][k] = mat[j][k]*a%MOD
                    for k in range(i,n+2):
                        mat[j][k] = (mat[j][k]*a - mat[i][i]*b)%MOD
    
    for i in range(1,n+1):
        if mat[i][i]!=0:
            flag = False
            for j in range(i+1,n+1):
                if mat[j][i]!=0:
                    flag = True
                    break
            
            if not flag:
                mat[i][n+1] = mat[i][n+1]*inv[mat[i][i]]%MOD
                mat[i][i] = 1
                
                    