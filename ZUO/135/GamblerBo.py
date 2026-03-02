import sys
import math

MOD = 3
dir4 = [0, -1, 0, 1, 0]

def build_inverse():
    inv = [0] * MOD
    inv[1] = 1
    for i in range(2, MOD):
        inv[i] = (MOD - inv[MOD % i] * (MOD // i) % MOD) % MOD
    return inv

def swap(mat, a, b):
    mat[a], mat[b] = mat[b], mat[a]

def prepare(n, m):
    s = n * m
    mat = [[0] * (s + 2) for _ in range(s + 1)]
    for i in range(n):
        for j in range(m):
            cur = i * m + j + 1
            mat[cur][cur] = 2
            for d in range(4):
                row = i + dir4[d]
                col = j + dir4[d + 1]
                if 0 <= row < n and 0 <= col < m:
                    mat[cur][row * m + col + 1] = 1
    return mat

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
                        mat[j][j] = mat[j][j] * a % MOD

                    for k in range(i, n + 2):
                        mat[j][k] = (mat[j][k] * a - mat[i][k] * b) % MOD

    for i in range(1, n + 1):
        if mat[i][i] != 0:
            mat[i][n + 1] = mat[i][n + 1] * inv[mat[i][i]] % MOD

def main():
    input = sys.stdin.readline
    inv = build_inverse()
    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        s = n * m
        mat = prepare(n, m)

        # 正确读入
        idx = 1
        for _ in range(n):
            row = list(map(int, input().split()))
            for v in row:
                mat[idx][s + 1] = (3 - v) % MOD
                idx += 1

        # 关键：必须消元
        gauss(mat, s, inv)

        ans = 0
        for i in range(1, s + 1):
            ans += mat[i][s + 1]

        print(ans)

        idx = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cnt = mat[idx][s + 1]
                for _ in range(cnt):
                    print(i, j)
                idx += 1

if __name__ == "__main__":
    main()