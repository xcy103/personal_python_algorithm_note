
#  高斯消元解决异或方程组模版题
#  有一个长度为n的数组arr，可能有重复值，数字都是long类型的正数
#  每个数拥有的质数因子一定不超过2000，每个数最多挑选一次
#  在至少要选一个数的情况下，你可以随意挑选数字乘起来
#  乘得的结果需要是完全平方数，请问有几种挑选数字的方法
#  方法数可能很大，答案对 1000000007 取模
#  1 <= n <= 300
#  1 <= arr[i] <= 10^18
#  测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5833

#思路就是，求最后自由元的数量，主元由自由元确定，一旦确定了自由元，主元也就确定了
#。。被gpt误导了，这里还是比较了之前的不是主元的行。
import sys
input = sys.stdin.readline

MOD = 1000000007
MAXV = 2000
MAXN = 305

#收集2000以内的质数，一共就303个，这是大于arr的个数的
def prepare():
    vis = [False]*(MAXV+1)
    prime = []
    for i in range(2,int(MAXV**0.5)+1):
        if not vis[i]:
            for j in range(i*i, MAXV+1):
                vis[j] = True
    
    for i in range(2,MAXV+1):
        if not vis[i]:
            prime.append(i)

prime = prepare()
cnt = len(prime)  
pow2 = [1]*(MAXN)
for i in range(1,MAXN):
    pow2[i] = pow2[i-1]*2%MOD

def gauss(mat,row,col):
    r = 0
    for c in range(col):
        pivot = -1
        for i in range(r,row):
            if mat[i][c]==1:
                pivot = i
                break
        if pivot==-1:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        for i in range(row):
            if i!=r and mat[i][c]==1:
                for j in range(c,col):
                    mat[i][j]^=mat[r][j]
        r+=1
    return r

#  影响每个主元的自由元们一旦确定
#  那么该主元选和不选也就唯一确定了
#  所以重点是自由元如何决策，n - main就是自由元的数量
#  自由元之间一定相互独立，每个自由元都可以做出选和不选的决定
#  所以一共是2的(n - main)次方种决策
#  但是想象一下，如果所有自由元都不选，
#  mat值的部分(cnt+1列)全是0啊！那么意味着，所有主元也都不选
#  但是题目要求至少要选一个数，所以不能出现自由元都不选的情况
#  所以返回方法数-1
#  能够分析的前提是对主元和自由元之间的关系有清晰的认识
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # 行 = 质数个数
    # 列 = n 个变量
    mat = [[0]*n for _ in range(cnt)]
    for i in range(n):
        cur = arr[i]
        for j in range(cnt):
            p = prime[j]
            if p*p>cur:break
            while cur%p==0:
                mat[j][i] ^= 1
                cur //= p
    m = gauss(mat,cnt,n)

    return (pow2[n-m] - 1)%MOD

t = int(input())
for case in range(1, t + 1):
    print(f"Case #{case}:")
    print(solve())