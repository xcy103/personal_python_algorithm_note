//这道题是不是求最大利润，是求，在保证利润不低于t的前提下
//能选的最少物品，并且这些物品总重量不超过s
//设计状态转移就是，前i号物品，选了k个，并且重量为w，
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    int N, S;
    long long T;
    cin >> N >> S >> T;

    vector<int> P(N), C(N), W(N);
    vector<long long> V(N);
    for (int i = 0; i < N; ++i) {
        cin >> P[i] >> C[i] >> W[i];
        V[i] = (long long)P[i] - C[i];
    }

    // dp[k][w] 表示选了 k 个物品，重量为 w 时的最大利润
    // 使用 vector 模拟 dp[N+1][S+1]
    vector<vector<long long>> dp(N + 1, vector<long long>(S + 1, -INF));
    dp[0][0] = 0;

    // 初始化 dp[0][0] = 0, 其他为 -INF
    for (int i = 0; i < N; ++i) { // 遍历物品
        for (int k = i + 1; k >= 1; --k) { // 数量倒序：更新“选 k 个”需要用到“选 k-1 个”的旧值
            for (int w = S; w >= W[i]; --w) { // 重量倒序：更新“重量 w”需要用到“重量 w-W[i]”的旧值
                if (dp[k - 1][w - W[i]] != -INF) {
                    dp[k][w] = max(dp[k][w], dp[k - 1][w - W[i]] + V[i]);
                }
            }
        }
}
    int ans = -1;
    for (int k = 0; k <= N; ++k) {
        for (int w = 0; w <= S; ++w) {
            if (dp[k][w] >= T) {
                ans = k;
                goto output; // 找到最小的 k 立即退出
            }
        }
    }

output:
    cout << ans << endl;

    return 0;
}