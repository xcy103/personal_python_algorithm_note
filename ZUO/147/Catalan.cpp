// 卡特兰数序列
// C(n):

// 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900 ...

// 对应 n =
// 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...


#include<bits/stdc++.h>
using namespace std;

using ll = long long;
const int MOD = 1e9 + 7;
const int MAXN = 1000001;

ll fac[MAXN];
ll inv1[MAXN];
//连续数字逆元
ll inv2[MAXN];


ll power(ll a,ll p){
    ll ans = 1;
    while(p){
        if(p&1){
            ans = (ans*a)%MOD;
        }
        a = (a*a)%MOD;
        p>>=1;
    }
    return ans;
}
// 构建阶乘和阶乘逆元
void build1(int n){
    fac[0] = fac[1] = inv1[0] = 1;
    for(int i=2;i<=n;i++){
        fac[i] = fac[i-1] * i % MOD;    
    }
    inv1[n] = pow(fac[n], MOD-2);
    for(int i=n-1;i>=1;i--){
        inv1[i] = (ll)inv1[i+1] * (i+1) % MOD;

    }
}
// 构建连续数逆元
void build2(int n){
    inv2[0] = inv2[1] = 1;
    for(int i=2;i<=n;i++){
        inv2[i] = MOD - inv2[MOD % i] * (MOD / i) % MOD;
    }
}

ll comb(int n,int k){
    return fac[n] * inv1[k] % MOD * inv1[n-k] % MOD;
}
//公式1
//C(n) = C(2n, n) - C(2n, n-1)
ll catalan1(int n){
    build1(2*n);
    return (comb(2*n, n) - comb(2*n, n-1) + MOD)%MOD;
}
//公式2
//C(n) = C(2n, n) / (n + 1)
ll catalan2(int n){
    build1(2*n);
    return (comb(2*n, n) * power(n+1,MOD-2)% MOD);
}
//公式3
//C(n) = C(n-1) * (4n - 2) / (n + 1)
ll catalan3(int n){
    build2(n);
    vector<ll> f(n+1);
    f[0] = f[1] = 1;
    for(int i=2;i<=n;i++){
        f[i] = ((f[i-1]*(4*i-2)%MOD)*inv2[i-1])%MOD;
    }
    return f[n];
    
}
//公式4
// C(n) = sum( C(i) * C(n-1-i) )
// i = 0 ... n-1
ll catalan4(int n){
    vector<ll> f(n+1);
    f[0] = f[1] = 1;
    for(int i=2;i<=n;i++){
        for(int l=0,r=i-1;l<i;l++,r--){
            f[i] = (f[i] + f[l]*f[r])%MOD;
        }
    }
    return f[n];
}
// 公式1 / 公式2 / 公式3 ： O(n)
// 公式4 ： O(n^2)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    cout << catalan1(n) << "\n";
    // cout << catalan2(n) << "\n";
    // cout << catalan3(n) << "\n";
    // cout << catalan4(n) << "\n";

    return 0;
}