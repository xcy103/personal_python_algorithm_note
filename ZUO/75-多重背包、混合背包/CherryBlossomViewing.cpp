#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100001;
const int MAXW = 1001;
const int ENOUGH = 1001;

int v[MAXN]; // 价值
int w[MAXN]; // 花费
int dp[MAXW];

int hour1, minute1, hour2, minute2;
int t, n, m;

// 01背包
int compute() {
    fill(dp, dp + t + 1, 0);
    for (int i = 1; i <= m; i++) {
        for (int j = t; j >= w[i]; j--) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }
    return dp[t];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        // 读取时间：hh:mm hh:mm
        char ch;

        if (!(cin >> hour1)) break; // EOF
        cin >> ch >> minute1;
        cin >> hour2 >> ch >> minute2;

        // 处理时间差
        if (minute1 > minute2) {
            hour2--;
            minute2 += 60;
        }
        t = (hour2 - hour1) * 60 + minute2 - minute1;

        cin >> n;
        m = 0;

        for (int i = 0; i < n; i++) {
            int cost, val, cnt;
            cin >> cost >> val >> cnt;

            if (cnt == 0) cnt = ENOUGH;

            // 二进制拆分
            for (int k = 1; k <= cnt; k <<= 1) {
                v[++m] = k * val;
                w[m] = k * cost;
                cnt -= k;
            }
            if (cnt > 0) {
                v[++m] = cnt * val;
                w[m] = cnt * cost;
            }
        }

        cout << compute() << '\n';
    }

    return 0;
}