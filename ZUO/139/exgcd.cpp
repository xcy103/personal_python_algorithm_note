#include<bits/stdc++.h>
using namespace std;
using ll=long long;
ll d,x,y,px,py;

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
        y = px - a/b*py;
    }
}