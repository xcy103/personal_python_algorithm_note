// 线段内部格点数 = gcd(dx, dy) - 1

// 包含端点 = gcd(dx, dy) + 1
#include<bits/stdc++.h>
using namespace std;
using ll=long long;

ll gcd(ll a, ll b){
    return b==0?a:gcd(b,a%b);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int cases;
    cin>>cases;

    for(int i=1;i<=cases;i++){
        ll x1,y1,x2,y2; 
        ll dx = llabs(x2-x1);
        ll dy = llabs(y2-y1);


        ll ans = gcd(dx,dy) + 1;
        cout<<"Case "<<i<<": "<<ans<<"\n";
    }
    return 0;
}