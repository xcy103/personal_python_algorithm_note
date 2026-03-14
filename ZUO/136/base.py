# 线性基常指的是异或空间线性基，向量空间线性基是下期的内容。
# 一堆数字能得到的非 0 异或和的结果，能被元素个数尽量少的集合，不多不少地全部得到。
# 那么就说，这个元素个数尽量少的集合，是这一堆数字的异或空间线性基。
# 注意，只关心去重的非 0 异或和能否全部得到，并不关心每种异或和的个数。
# 如下几个结论是构建异或空间线性基的基础：
# 一堆数字中，任意的 a 和 b，用 a ^ b 的结果替代 a、b 中的一个数字，不会影响异或和的组成。
# 一堆数字中，任意的 a 和 b，如果有 a ^ b = 0，那么舍弃掉 a、b 其中一个数字，不会影响异或和的组成。
# 一堆数字能否异或出 0，在求出异或空间线性基之后，需要被单独标记。
# 如何找第k小，把k表示成2进制，哪一位上有1就异或上这一大小的线性基
# 注意，普通消元得到的线性基，不能这么求，是不准的，只有高斯消元
# 得到的线性基可以这么求
# 线性基的个数如果和数组最大值的个数一样多，就是没有0的

# 异或空间线性基
# 包含：
# 1. 普通消元
# 2. 高斯消元（简化版）

MAXN = 101
BIT = 60
# ==============================
# 普通消元（插入式线性基）
# ==============================

basis1 = [0] * (BIT + 1)
zero1 = False

def insert1(num):
    """
    向线性基中插入 num
    成功插入返回 True
    如果插入失败（说明线性相关）返回 False
    """
    for i in range(BIT, -1, -1):
        if num>>i&1:
            if basis1[i]==0:
                basis1[i] = num
                return True
            num^=basis1[i]
    return False

def compute1(arr):
    """
    普通消元构建线性基
    arr: 输入数组
    返回：
        basis1
        zero1 (是否可以异或出 0)
    """
    global basis1, zero1
    basis1 = [0] * (BIT + 1)
    zero1 = False
    for num in arr:
        if not insert1(num):
            zero1 = True
    return basis1, zero1

# ==============================
# 高斯消元（矩阵式构建）
# ==============================
basis2 = [0] * MAXN
len_basis = 0
zero2 = False

def compute2(arr):
    """
    高斯消元构建线性基
    arr: 输入数组
    返回：
        basis2[0:len_basis]
        zero2 (是否可以异或出 0)
    """
    global basis2, len_basis, zero2

    n = len(arr)
    basis2 = arr[:] + [0]*(MAXN-n)
    row = 0
    for bit in range(BIT, -1, -1):
        povit = -1
        for i in range(row,n):
            if(basis2[i]>>bit)&1:
                povit = i
                break
        if povit == -1:
            continue
        basis2[povit], basis2[row] = basis2[row], basis2[povit]
        for i in range(n):
            if i!=row and ((basis2[i]>>bit)&1):
                basis2[i]^=basis2[row]
        row+=1
    len_basis = row
    zero2 = (len_basis!=n)

    return basis2[0:len_basis], zero2