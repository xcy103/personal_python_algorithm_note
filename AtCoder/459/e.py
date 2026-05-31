import sys
sys.setrecursionlimit(200000)
#有10**9!!!怎么办
mod = 998244353

def ksm(a,p):
    ans = 1
    while p:
        if p&1: ans = (ans*a)%mod
        p>>=1
        a = (a*a)%mod
    return ans
fac = [1]*(10**6+1)
inv = [1]*(10**6+1)
for i in range(2,10**6+1):
    fac[i] = fac[i-1]*i%mod
inv[i]
n = int(input())
inv[-1] = ksm(fac[-1],mod-2)
for i in range(len(inv)-2,-1,-1):
    inv[i] = inv[i+1]*(i+1)%mod

def comb(n,m):
    return fac[n]*inv[m]*inv[n-m]%mod
p = [-1]+list(map(int,input().split()))
candy = list(map(int,input().split()))
ins = list(map(int,input().split()))

#从0开始
size1 = [0]*n
size2 = [0]*n
size3 = [0]*n
g = [[] for _ in range(n)]
for i in range(1,n):
    g[p[i]-1].append(i)

def dfs_candy(u):
    size1[u] = candy[u]
    for v in g[u]:
        size1[u]+=dfs_candy(v)
    return size1[u]
dfs_candy(0)

def dfs_ins(u):
    size2[u] = ins[u]
    for v in g[u]:
        size2[u]+=dfs_ins(v)
    return size2[u]
dfs_ins(0)
for i in range(n):
    if size1[i]<size2[i]:
        print(0)
        exit(0)

def dfs(u):
    if len(g[u])==0:
        size3[u] = size1[u]
        return ins[u]
    size = 0
    for v in g[u]:
        size+=dfs(v)
    size3[u] = size1[u] - size
    return size2[u] 
dfs(0)
# print(size3)
# print(ins)
#就是从这两个数组里，搞，最后的结果
#上面的是n，下面的是m

import sys
# 题目树高可达 2*10^5，提高递归深度并扩大栈空间
sys.setrecursionlimit(300000)

mod = 998244353
max_d = 10**6

# 1. 预处理 1 到 10^6 的阶乘与逆元（仅用于组合数分母）
fac = [1] * (max_d + 1)
inv = [1] * (max_d + 1)
for i in range(2, max_d + 1):
    fac[i] = fac[i-1] * i % mod

# 快速幂
inv[max_d] = pow(fac[max_d], mod - 2, mod)
for i in range(max_d - 1, -1, -1):
    inv[i] = inv[i+1] * (i + 1) % mod

# 2. 核心：大 n 小 m 组合数函数，通过循环 O(m) 计算分子
def comb_large(n_total, m_select):
    if n_total < m_select: return 0
    if m_select == 0: return 1
    numerator = 1
    for i in range(m_select):
        numerator = numerator * ((n_total - i) % mod) % mod
    return numerator * inv[m_select] % mod

# --- 以下完全保留你的输入与图的建立 ---
n = int(input())
p = [-1] + list(map(int, input().split()))
candy = list(map(int, input().split()))
ins = list(map(int, input().split()))

size1 = [0] * n  # 子树糖果总数
size2 = [0] * n  # 子树需求总数
g = [[] for _ in range(n)]
for i in range(1, n):
    g[p[i]-1].append(i)

# --- 合并你的 DFS：一次 DFS 同时统计 size1 和 size2 ---
def dfs_init(u):
    size1[u] = candy[u]
    size2[u] = ins[u]
    for v in g[u]:
        dfs_init(v)
        size1[u] += size1[v]
        size2[u] += size2[v]

dfs_init(0)

# 合法性校验
for i in range(n):
    if size1[i] < size2[i]:
        print(0)
        exit(0)

# --- 3. 乘法原理统计最终结果 ---
ans = 1
for i in range(n):
    # 当前节点可用糖果 = 子树总糖果 - 子树总需求 + 当前节点自身需求
    available = size1[i] - size2[i] + ins[i]
    ans = ans * comb_large(available, ins[i]) % mod

print(ans)