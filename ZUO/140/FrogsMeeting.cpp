#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll d,x,y;

void exgcd(ll a,ll b){
    if(b==0){
        d = a;
        x = 1;
        y = 0;
    }else{
        exgcd(b,a%b);
        ll px = x;
        ll py = y;
        x = py;
        y = px - (a/b)*py;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll x1,x2,m,n,l;
    cin>>x1>>x2>>m>>n>>l;

    ll a,c;

    if(x1<x2){
        a = m-n;
        c = x2-x1;
    }else{
        a = n-m;
        c = x1-x2;
    }

    if(a<0){
        a = -a;
        c = l-c;
    }
    exgcd(a,l);
    if (c % d != 0) {
        cout << "Impossible\n";
        return 0;
    }
    ll t0 = c / d * x;
    ll step = l / d;
    if(t0<0){
        t0+=(1-t0 + step - 1)/ step * step;
    }else{
        t0-=(t0-1)/ step * step;
    }
    cout << t0 << "\n";
    return 0;
}