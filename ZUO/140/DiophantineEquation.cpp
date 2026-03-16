// 扩展欧几里得和二元一次不定方程

// 二元一次不定方程，也叫丢番图方程（Diophantine Equation），ax + by = c  
// 扩展欧几里得算法可以对二元一次不定方程进行解如何变化的讨论。

// a 和 b 是不全为 0 的整数，d 为 a 和 b 的最大公约数。

// 如果 ax + by = c，c 不是 d 的整数倍，那么方程无整数解，否则有无穷多整数解。这是上节课内容。

// 如果 ax + by = d，d 为 gcd(a, b)，其中一个特解是 (x0, y0)

// 那么通解可以表示为：
// x = x0 + (b / d) * n
// y = y0 - (a / d) * n
// n 为任意整数

// 如果 ax + by = c，c 为 d 的整数倍，根据上面的特解，可以得到该等式的一个特解 (x0', y0')

// 其中：
// x0' = x0 * (c / d)
// y0' = y0 * (c / d)

// 那么通解可以表示为：
// x = x0' + (b / d) * n
// y = y0' - (a / d) * n
// n 为任意整数

// 二元一次不定方程模版
// 给定a、b、c，求解方程ax + by = c
// 如果方程无解打印-1
// 如果方程无正整数解，但是有整数解
// 打印这些整数解中，x的最小正数值，y的最小正数值
// 如果方程有正整数解，打印正整数解的数量，同时打印所有正整数解中，
// x的最小正数值，y的最小正数值，x的最大正数值，y的最大正数值
// 1 <= a、b、c <= 10^9
// 测试链接 : https://www.luogu.com.cn/problem/P5656
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
            // x要想增长到>=1且最小的值，差几个xd，算出来就是k的值
			// 那应该是(1-x)/xd，结果向上取整
            times = (1-x + xd-1)/xd;
            x+= times*xd;
            y-= times*yd;
        }else{
            // x要想减少到>=1且最小的值，差几个xd，算出来就是k的值，向下取整
            times = (x-1)/xd;
            x-= times*xd;
            y+= times*yd;
        }
        if(y<=0){
            // 无正整数解
            cout << x << " ";
            cout << y + yd * ((1 - y + yd - 1) / yd) << "\n";
        }else{
            // y减少到1以下，能减几次，就是正整数解的个数
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