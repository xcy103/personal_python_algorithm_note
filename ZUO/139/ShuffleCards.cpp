//我们通过观察发现，每次洗牌的位置，拿1举例，会乘2
//然后再mod一个（n+1）我们知道洗牌次数，以及最后的位置
//相当于使用拓展欧几里得找出一组解 (x*2^m + y*(n+1))==l
//因为2^m和(n+1)互质，所以可以求(x*2^m + y*(n+1))==1
//得到x，x乘l再mod（n+1）得到结果

#include<iostream>
using namespace std;
#define ll long long

ll d,x,y,px,py;

//拓展欧几里得
void exgcd(ll a,ll b){
    if(b==0){
        d = a;
        x = 1;
        y = 0;
    }else{
        exgcd(b,a%b);
        px = x;
        py = y;
        x = py;
        y = px - (a/b)*py;
    }
}

ll multiply(ll a,ll b, ll mod){
    a = (a%mod + mod)%mod;
    b = (b%mod + mod)%mod;
    ll ans = 0;
    while(b){
        if(b&1) ans = (ans+a)%mod;
        a = (a+a)%mod;
        b >>= 1;
    }
    return ans;
}
ll power(ll a,ll b, ll mod){
    ll ans = 1;
    while(b){
        if(b&1) ans = multiply(ans,a,mod);
        a = multiply(a,a,mod);
        b >>= 1;
    }
    return ans;
}

ll compute(ll n, ll m,ll l){
    ll mod = n+1;
    ll p = power(2,m,mod);
    exgcd(p,mod);
    ll inv = (x%mod + mod)%mod;
    return multiply(inv,l,mod);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n,m,l;
    cin >> n >> m >> l;
    cout << compute(n,m,l) << "\n";
    return 0;
}