#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1001;
const int MAXM = 500001;
using ll = long long;

int n, w, m;
ll dp[MAXM], cost[MAXN], val[MAXN];

ll compute(){
    fill(dp, dp + w + 1, LLONG_MAX);
    dp[0] = 0;

    for(int i = 1; i <= m; i++){
        for(int j = w; j >= cost[i]; j--){
            if(dp[j - cost[i]] != INT_MAX){
                dp[j] = min(dp[j], dp[j - cost[i]] + val[i]);
            }
        }
    }
    return dp[w];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> w;

    for(int i = 1; i <= n; i++){
        int l, c;
        cin >> l >> c;

        // 二进制拆分
        for(int k = 1; k <= c; k <<= 1){
            cost[++m] = 1LL*k * l;
            val[m] = k;
            c -= k;
        }
        if(c){
            cost[++m] = 1LL*c * l;
            val[m] = c;
        }
    }

    ll ans = compute();
    ans = (ans == LLONG_MAX ? -1 : ans);
    cout << ans << "\n";

    return 0;
}