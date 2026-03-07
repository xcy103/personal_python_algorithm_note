#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 20100403;
const int MAXN = 2000001;

ll fac[MAXN];
ll inv[MAXN];

ll power(ll a, ll p){
    ll ans = 1;
    while(p){
        if(p&1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        p >>= 1;
    }
    return ans;
}

void build(int n){
    fac[0] = fac[1] = inv[0] = 1;
    for(int i = 2; i <= n; i++){
        fac[i] = (fac[i-1] * i) % MOD;

    }
    inv[n] = power(fac[n], MOD-2);
    for(int i = n-1; i >= 1; i--){
        inv[i] = (1LL*inv[i+1] * (i+1)) % MOD;
    }
}
ll comb(int n,int k){
    return (fac[n] * (inv[k] * inv[n-k] % MOD)) % MOD;
}

ll compute(int n, int m){
    build(n+m);
    return (comb(n+m,m) - comb(n+m, m-1) + MOD) % MOD;
}

int main(){ 
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,m;
    cin>>n>>m;
    cout<<compute(n,m)<<"\n";
    return 0;
}
