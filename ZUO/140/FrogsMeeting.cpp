// 青蛙的约会
// 有一个周长为l的环，从环的0位置开始，规定只能沿着顺时针方向不停转圈
// 青蛙A在环的x1位置，每秒跳m个单位，青蛙B在x2位置，每秒跳n个单位
// 只有在某时刻，青蛙A和青蛙B来到环的同一个位置，才算相遇
// 如果两只青蛙相遇不了，打印"Impossible"
// 如果可以相遇，打印两只青蛙至少多久才能相遇
// 1 <= l <= 3 * 10^9
// 1 <= x1、x2、m、n <= 2 * 10^9
// x1 != x2
// 测试链接 : https://www.luogu.com.cn/problem/P1516
//这里一定要纠结谁在追谁，因为拓展欧几里得的系数一定不能为负数
//一定要注意，特解调整为最小正整数解应该向上取整
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