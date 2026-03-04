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

    int cases;
    cin >> cases;

    while(cases--){
        ll a,b,c;
        cin >> a >> b >> c;
        exgcd(a,b);
        if(c%d){
            cout << -1 << "\n";
            continue;
        }
        x*=c/d;
        y*=c/d;

        ll xd = b/d;
        ll yd = a/d;

        ll times;

        if(x<0){
            times = (1-x + xd-1)/xd;
            x+= times*xd;
            y-= times*yd;
        }else{
            times = (x-1)/xd;
            x-= times*xd;
            y+= times*yd;
        }
        if(y<=0){
            // 无正整数解
            cout << x << " ";
            cout << y + yd * ((1 - y + yd - 1) / yd) << "\n";
        }else{
            ll cnt = (y - 1) / yd + 1;
            cout << cnt << " ";
            // x最小正整数
            cout << x << " ";
            // y最小正整数
            cout << y - (y - 1) / yd * yd << " ";
            // x最大正整数
            cout << x + (y - 1) / yd * xd << " ";
            // y最大正整数
            cout << y << "\n";
        }
        
    }
    return 0;
}