//中国剩余定理基础模板，需要满足m1-mn两两互质
#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int MAXN = 11;

ll m[MAXN],r[MAXN],d,x,y,n;

void exgcd(ll a,ll b){
    if(b==0){
        d = a,x = 1,y = 0;
    }else{
        exgcd(b,a%b);
        ll px = x;
        ll py = y;
        x = py;
        y = px - (a/b)*py;
    }
}
ll multiply(ll a,ll b,ll mod){
    a = (a%mod + mod)%mod;
    b = (b%mod + mod)%mod;
    ll ans = 0;
    while(b){
        if(b&1){
            ans = (ans + a)%mod;
        }
        a = (a + a)%mod;
        b >>= 1;
    }
    return ans;
}

ll crt(int n){
    ll lcm = 1;
    for(int i=1;i<=n;i++){
        lcm*=m[i];
    }
    ll ans = 0;
    for(int i=1;i<=n;i++){
        ll ai = lcm/m[i];
        exgcd(ai,m[i]);
        ll inv = (x%m[i] + m[i])%m[i];
        ll ci = multiply(r[i],multiply(ai,inv,lcm),lcm);
        ans = (ans + ci)%lcm;
    }
    return (ans%lcm + lcm)%lcm;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>m[i]>>r[i];
    }
    cout<<crt(n)<<"\n";
    return 0;
}
