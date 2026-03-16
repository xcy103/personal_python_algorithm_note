//边上的格点就是两个点横纵坐标之间差求gcd
//面积就是鞋带公式
//顺：每一项（X后Y前 - X前Y后）累加起来
// 逆：每一项（X前Y后 - X后Y前）累加起来
//面积 = 内部格点数 + 外部格点数/2 - 1(Pick定理)
//证明就是把多边形分为n个的面积为1/2小三角，这些小三角
//都是由内部的格点和外部的格点联系起来的

#include<bits/stdc++.h>
using namespace std;
using ll = long long;
ll gcd(ll a,ll b){
    return b?gcd(b,a%b):a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        int n;
        cin>>n;
        ll edges;
        double area = 0;
        ll x = 0,y = 0;
        for(int i=1;i<=n;i++){
            ll dx,dy;
            cin>>dx>>dy;
            edges = gcd(abs(dx),abs(dy));

            area = x*(y+dy) - y*(x+dx);
            x+=dx;
            y+=dy;
        }
        area/=2.0;
        int inners = (int) area - edges/2 + 1;
        cout << "Scenario #" << t << ":\n";
        cout << inners << " " << edges << " ";
        cout << fixed << setprecision(1) << area << "\n\n";
    }
    return 0;
    
}