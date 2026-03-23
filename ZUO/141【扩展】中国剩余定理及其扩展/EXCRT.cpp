//拓展中国剩余定理模板，不用满足m1-mn两两互质
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
        //第一步，找出b,c ax + by = c (mod b)最初的a就是lcm
        ll b = m[i];
        ll c = ((r[i] - tail)%b+b)%b;

        exgcd(lcm,b);
        if (c % d != 0) {
            return -1;
        }
        
        //求出最小非负特解
        ll mod = b/d;
        ll x0 = multiply(x,c/d,mod);
        //这里的lcm就是a
        //反正很奇怪，为什么tmp不需要用龟速乘法，因为找不到mod
        //噢我知道了，这里的x0取模是因为结论，
        //下面的tail取模是因为要找到最小的tail
        //求出最小非负解之后，就要带入回原始，只含有x的方程

        // ans = lcm * x + tail，带入通解
        // ans = lcm * (x0 + (b/d) * n) + tail
        // ans = lcm * (b/d) * n + lcm * x0 + tail
        // tail' = tail' % lcm'
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