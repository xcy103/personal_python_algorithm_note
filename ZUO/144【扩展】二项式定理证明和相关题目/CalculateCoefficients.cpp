#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXK = 1001;
const int MOD = 10007;

ll fac[MAXK+1],inv[MAXK+1];
int a,b,k,n,m;

ll power(ll x,int p){
    ll ans = 1;
    while(p){
        if(p&1) ans = ans * x % MOD;
        x = x * x % MOD;
        p >>= 1;
    }
    return ans;
}

void build(){
    fac[0] = 1;
    for(int i=1;i<=MAXK;i++){
        fac[i] = fac[i-1] * i % MOD;
    }
    inv[MAXK] = power(fac[MAXK],MOD-2);
    for(int i=MAXK-1;i>=0;i--){
        inv[i] = inv[i+1] * (i+1) % MOD;
    }
}

ll comb(int n,int k){
    return fac[n] * inv[k] % MOD * inv[n-k] % MOD;
}
ll compute(){
    build();
    return power(a,n)*power(b,m)%MOD*comb(k,k-n)%MOD;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>a>>b>>k>>n>>m;
    cout<<compute()<<"\n";
    return 0;
}