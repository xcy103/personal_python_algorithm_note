#include<bits/stdc++.h>
using namespace std;
#define ll long long

const int MAXN = 100001;

ll hp[MAXN];
ll recovery[MAXN];
ll reward[MAXN];
ll init[MAXN];
ll attack[MAXN];

map<ll,int> sorted_map;

ll d,x,y;

void exgcd(ll a, ll b){
    if(b==0){
        d = a,x = 1,y = 0;
    }else{
        exgcd(b,a%b);
        ll px = x,py = y;
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
            ans = (ans+a)%mod;
        }
        a = (a+a)%mod;
        b >>= 1;
    }
    return ans;
}

ll allocate(int n,int m){
    sorted_map.clear();
    for(int i=1;i<=m;i++){
        sorted_map[init[i]]++;
    }
    ll mx = 0;
    for(int i=1;i<=n;i++){
        auto it = sorted_map.upper_bound(hp[i]);

        ll sword;
        if(it==sorted_map.begin()){
            sword = sorted_map.begin()->first; 
        }else{
            --it;
            sword = it->first;
        }

        attack[i] = sword;
        if(--sorted_map[sword]==0){
            sorted_map.erase(sword);
        }
        sorted_map[reward[i]]++;
        mx = max(mx,(hp[i]+attack[i]-1)/attack[i]);
        hp[i]%=recovery[i];
    }
    return mx;
}

ll compute(int n,int m){
    ll mx = allocate(n,m);
    ll tail = 0, lcm = 1;
    ll tmp,a,b,c,x0;
    for(int i=1;i<=n;i++){
        a = multiply(attack[i],lcm,recovery[i]);
        b = recovery[i];
        c = ((hp[i] - attack[i]*tail)%b + b)%b;

        exgcd(a,b);
        if(c%d){
            return -1;
        }

        x0 = multiply(x,c/d,b/d);
        tmp = lcm*(b/d);
        tail = (tail + multiply(x0,lcm,tmp))%tmp;
        lcm = tmp;
    }
    ll ans;
    if(tail>=mx){
        ans = tail;
    }else{
        ans = (mx-tail + lcm-1)/lcm*lcm + tail;
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int cases;
    cin>>cases;
    while(cases--){
        int n,m;
        cin>>n>>m;
        for(int i=1;i<=n;i++)
            cin>>hp[i];

        for(int i=1;i<=n;i++)
            cin>>recovery[i];

        for(int i=1;i<=n;i++)
            cin>>reward[i];

        for(int i=1;i<=m;i++)
            cin>>init[i];
       
        cout<<compute(n,m)<<"\n";
    }
    return 0;
}

