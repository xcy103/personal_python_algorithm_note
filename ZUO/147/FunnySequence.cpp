#include<bits/stdc++.h>
using namespace std;

using ll = long long;
const int MAXN = 2000001;

int minpf[MAXN];
int prime[MAXN];
int cnt;
int counts[MAXN];

void euler(int n){
    fill(minpf+2, minpf+n+1, 0);
    cnt = 0;
    for(int i = 2; i <= n; i++){
        if(minpf[i] == 0){
            prime[cnt++] = i;
        }
        for(int j=0;j<cnt;j++){
            ll x = 1LL * i * prime[j];
            if(x > n) break;
            minpf[x] = prime[j];
            if(i % prime[j] == 0) break;
        }
    }
}

ll power(ll x,ll p, ll mod){
    ll ans = 1;
    while(p){
        if(p&1) ans = ans * x % mod;
        x = x * x % mod;
        p >>= 1;
    }
    return ans;
}
int compute(int n,int mod){
    euler(2*n);
    fill(counts+2, counts+n+1, -1);
    fill(counts+n+2, counts+2*n+1, 1);

    for(int i=2*n;i>=2;i--){
        if(minpf[i]!=0){
            counts[minpf[i]] += counts[i];
            counts[i/minpf[i]] +=counts[i];
            counts[i]=0;
        }
    }

    ll ans = 1;

    for(int i=2;i<=2*n;i++){
        if(counts[i]){
            ans = ans * power(i,counts[i],mod) % mod;
        }

    }
    return (int)ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, mod;
    cin>>n>>mod;
    cout<<compute(n,mod)<<"\n";
    return 0;
}