#  有一次错误称重求最重物品
#  一共有n个物品，编号1~n，定义合法方案如下：
#  1，每个物品的重量都是确定的
#  2，每个物品的重量一定都是正整数
#  3，最重的物品有且仅有1个
#  每次称重格式类似：3 2 5 6 10，代表本次称重涉3个物品，编号为2、5、6，总重量10
#  一共有n+1条称重数据，称重数据整体有效的条件为：
#  错误的称重数据有且仅有1条，只有排除这条错误称重，才能求出一种合法方案
#  如果称重数据有效，打印最重三角形的编号
#  如果称重数据无效，打印"illegal"
#  1 <= m <= n <= 100
#  测试链接 : https://www.luogu.com.cn/problem/P5027
import sys

MAXN = 102
sml = 1e-7
input = sys.stdin.readline
n = int(input().strip())

data = [[0]*(n+2) for _ in range(n+2)]
mat = [[0.0]*(n+2) for _ in range(n+2)]

for i in range(1,n+2):
    arr = list(map(int,input.split()))
    m = arr[0]
    for j in range(1,m+1):
        cur = arr[j]
        data[i][cur] = 1
    data[i][n+1] = arr[m+1]

def gauss(n):
    for i in range(1,n+1):
        max_row = i
        for j in range(1,n+1):
            if j<i and abs(mat[j][j])>=sml:
                continue
            if abs(mat[j][i]) > abs[max_row][i]:
                max_row = j
        
        mat[i],mat[max_row] = mat[max_row],mat[i]

        if abs(mat[i][i])>=sml:
            pivot = mat[i][i]
            for j in range(1,n+2):
                mat[i][j]/=pivot
            
            for j in range(1,n+1):
                if i==j:continue
                
                rate = mat[j][i]
                for k in range(1,n+2):
                    mat[j][k]-=rate*mat[j][i]


def check():
    gauss(n)
    maxv = -1
    maxt = 0
    ans = 0

    for i in range(1,n+1):
        if abs(mat[i][i])<sml:
            return 0
        val = mat[i][n+1]
        if val<=0 or abs(val-int(val))>sml:
            return 0
        val = int(round(val))
        if val>maxv:
            maxt = 1
            maxv = val
            ans = i
        elif val == maxv:
            maxt+=1
    
    if maxt>1:
        return 0
    return ans

ans = 0
times = 0
for k in range(1,n+2):
    data[k], data[n+1] = data[n+1], data[k]

    for i in range(1,n+1):
        for j in range(1,n+2):
            mat[i][j] = float(data[i][j])
    
    data[k], data[n+1] = data[n+1], data[k]
    cur = check()
    if cur!=0:
        times+=1
        ans = cur

if times != 1:
    print("illegal")
else:
    print(ans)

