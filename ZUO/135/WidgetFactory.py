#  工具工厂
#  一共有n种工具，编号1~n，一共有m条记录，其中一条记录格式如下：
#  4 WED SUN 13 18 1 13
#  表示有个工人一共加工了4件工具，从某个星期三开始工作，到某个星期天结束工作
#  加工的工具依次为13号、18号、1号、13号
#  每个工人在工作期间不休息，每件工具都是串行加工的，完成一件后才开始下一件
#  每种工具制作天数是固定的，并且任何工具的制作天数最少3天、最多9天
#  但该数据丢失了，所以现在需要根据记录，推断出每种工具的制作天数
#  如果记录之间存在矛盾，打印"Inconsistent data."
#  如果记录无法确定每种工具的制作天数，打印"Multiple solutions."
#  如果记录能够确定每种工具的制作天数，打印所有结果
#  1 <= n、m <= 300
#  测试链接 : http://poj.org/problem?id=2947
import sys
import math

MOD = 7
MAXN = 305

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

def build_inverse():
    inv = [0] * MOD
    inv[1] = 1
    for i in range(2, MOD):
        inv[i] = (MOD - inv[MOD % i] * (MOD // i) % MOD) % MOD
    return inv

def day_index(s):
    return days.index(s)

def swap(mat, a, b):
    mat[a], mat[b] = mat[b], mat[a]

def gauss(mat, n, inv):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j < i and mat[j][j] != 0:
                continue
            if mat[j][i] != 0:
                swap(mat, i, j)
                break

        if mat[i][i] != 0:
            for j in range(1, n + 1):
                if i != j and mat[j][i] != 0:
                    g = math.gcd(mat[j][i], mat[i][i])
                    a = mat[i][i] // g
                    b = mat[j][i] // g

                    if j < i and mat[j][j] != 0:
                        for k in range(j, i):
                            mat[j][k] = mat[j][k] * a % MOD

                    for k in range(i, n + 2):
                        mat[j][k] = (mat[j][k] * a - mat[i][k] * b) % MOD

    for i in range(1, n + 1):
        if mat[i][i] != 0:
            free = False
            for j in range(i + 1, n + 1):
                if mat[i][j] != 0:
                    free = True
                    break
            if not free:
                mat[i][n + 1] = mat[i][n + 1] * inv[mat[i][i]] % MOD
                mat[i][i] = 1


def main():
    input = sys.stdin.readline
    inv = build_inverse()

    while True:
        line = input()
        if not line:
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        s = max(n, m)
        mat = [[0] * (s + 2) for _ in range(s + 1)]

        for i in range(1, m + 1):
            parts = input().split()
            k = int(parts[0])
            st = parts[1]
            et = parts[2]

            idx = 3
            for _ in range(k):
                tool = int(parts[idx])
                idx += 1
                mat[i][tool] = (mat[i][tool] + 1) % MOD

            mat[i][s + 1] = (day_index(et) - day_index(st) + 1) % MOD

        gauss(mat, s, inv)

        sign = 1
        for i in range(1, s + 1):
            if mat[i][i] == 0 and mat[i][s + 1] != 0:
                sign = -1
                break
            if i <= n and mat[i][i] == 0:
                sign = 0

        if sign == -1:
            print("Inconsistent data.")
        elif sign == 0:
            print("Multiple solutions.")
        else:
            ans = []
            for i in range(1, n + 1):
                val = mat[i][s + 1]
                if val < 3:
                    val += 7
                ans.append(str(val))
            print(" ".join(ans))


if __name__ == "__main__":
    main()