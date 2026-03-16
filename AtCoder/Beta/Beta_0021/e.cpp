//矩阵快速幂优化，有点不太懂
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

// 定义极小值，用于矩阵初始化（类似加法中的0）
const ll INF = 2e18; // 足够小但不会溢出

// 2x2 矩阵结构体
struct Matrix {
    ll mat[2][2];
    Matrix() {
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                mat[i][j] = -INF;
    }
};

// 重载 (max, +) 矩阵乘法
Matrix multiply(Matrix A, Matrix B) {
    Matrix C;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                // 传统 C[i][j] += A[i][k] * B[k][j] 
                // 变为 C[i][j] = max(C[i][j], A[i][k] + B[k][j])
                if (A.mat[i][k] != -INF && B.mat[k][j] != -INF) {
                    C.mat[i][j] = max(C.mat[i][j], A.mat[i][k] + B.mat[k][j]);
                }
            }
        }
    }
    return C;
}

// 矩阵快速幂
Matrix power(Matrix A, ll p) {
    Matrix res;
    // 单位矩阵在 (max, +) 中对角线为 0
    res.mat[0][0] = 0; res.mat[1][1] = 0;
    
    while (p > 0) {
        if (p & 1) res = multiply(res, A);
        A = multiply(A, A);
        p >>= 1;
    }
    return res;
}

int main() {
    ll N, a, b;
    if (!(cin >> N >> a >> b)) return 0;

    if (N == 1) {
        cout << max(a, b) << endl;
        return 0;
    }

    // 构建转移矩阵 M
    // 状态 0: 选 Method B, 状态 1: 选 Method A
    // M[next_state][prev_state]
    Matrix M;
    M.mat[0][0] = b;          // B -> B
    M.mat[0][1] = b / 2;      // A -> B
    M.mat[1][0] = a;          // B -> A
    M.mat[1][1] = a / 2;      // A -> A

    // 计算 M 的 N-1 次方
    Matrix res = power(M, N - 1);

    // 初始状态 (Day 1)
    ll dp1_0 = b; // 第一天选 B
    ll dp1_1 = a; // 第一天选 A

    // 最终结果向量 V_n = M^(N-1) * V_1
    ll ans_0 = max(res.mat[0][0] + dp1_0, res.mat[0][1] + dp1_1);
    ll ans_1 = max(res.mat[1][0] + dp1_0, res.mat[1][1] + dp1_1);

    cout << max(ans_0, ans_1) << endl;

    return 0;
}