//中国剩余定理基础模板，需要满足m1-mn两两互质
// 中国剩余定理及其扩展

// 中国剩余定理
// 给出 n 个同余方程，m1, m2, ... , mn 一定两两互质，
// 求满足同余方程的最小正数解 x

// x ≡ r1 (mod m1)
// x ≡ r2 (mod m2)
// x ≡ r3 (mod m3)
// ...
// x ≡ rn (mod mn)

// 求解的原理：
// x = c1 + c2 + c3 + ... + cn

// 如果 i ≠ j，
// ci % mi = ri
// ci % mj = 0

// 则 x 满足所有同余方程。

// 当 m1, m2, ... , mn 一定两两互质时，必存在这样的 x。
// 根据如下过程就可以求出这样的 x，并且是最小正数解。

// 求解过程：

// 1. 计算 M = m1 * m2 * ... * mn  
//    因为 m1, m2, ... , mn 一定两两互质，所以结果为最小公倍数 lcm。

// 2. 对每一个同余方程计算：

//    ai = M / mi  
//    ai逆元 = ai 在 mod mi 意义下的逆元  

//    ci = (ri * ai * ai逆元) % M

// 3. 最小正数解：

//    x = (c1 + c2 + ... + cn) % M
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
ll mul(ll a,ll b,ll mod){
    ll ans = 0;
    while(b){
        if(b&1) ans = (ans + a)%mod;
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
        ll ci = mul(r[i],mul(ai,inv,lcm),lcm);
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

// 讲解扩展中国剩余定理之前，先介绍一个关于扩展欧几里得算法的小结论

// 如果 ax + by = d，d 为 gcd(a, b)，其中一个特解是 (x0, y0)

// 那么通解可以表示为：
// x = x0 + (b / d) * n
// y = y0 - (a / d) * n
// n 为任意整数

// 如果 ax + by = c，c 为 d 的整数倍，
// 根据上面的特解，可以得到该等式的一个特解 (x0', y0')

// 其中：
// x0' = x0 * (c / d)
// y0' = y0 * (c / d)

// 那么通解可以表示为：
// x = x0' + (b / d) * n
// y = y0' - (a / d) * n
// n 为任意整数

// 以上都是，讲解140 - 扩展欧几里得和二元一次不定方程，讲的内容

// 其中通解：
// x = x0' + (b / d) * n

// 如何得到最小非负特解？利用如下公式：

// 最小非负特解 = x0' % (b / d)，取非负余数