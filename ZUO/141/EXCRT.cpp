#include<bits/stdc++.h>
using namespace std;
#define ll long long

const int MAXN = 100001;
ll m[MAXN],r[MAXN],d,x,y;

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

ll multiply(ll a, ll b, ll mod){
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

ll excrt(int n){
    ll lcm = 1;
    ll tail = 0;

    for(int i=1;i<=n;i++){
        ll b = m[i];
        ll c = ((r[i]-tail)%b + b)%b;

        exgcd(lcm,b);

        if(c%d!=0){
            return -1;
        }

        ll mod = b/d;
        ll x0 = multiply(x,c/d,mod);

        ll tmp = lcm*mod;
        tail = (tail + multiply(x0,lcm,tmp))%tmp;
        lcm = tmp;
    }
    return (tail%lcm + lcm)%lcm;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>m[i]>>r[i];
    }
    cout<<excrt(n)<<"\n";
    return 0;
}