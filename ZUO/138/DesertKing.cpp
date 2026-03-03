// 最优比率生成树
// 一共有n个村庄，每个村庄由(x, y, z)表示
// 其中(x,y)代表村庄在二维地图中的位置，z代表其海拔高度
// 任意两个村庄之间的距离就是二维地图中的欧式距离
// 任意两个村庄之间的修路花费就是海拔差值的绝对值
// 现在想把所有村庄连通起来，希望修路的条数尽量少，同时希望让
// 总花费 / 总距离，这个比值尽量小，返回最小的比值是多少，结果保留小数点后3位其余部分舍弃
// 2 <= n <= 10^3
// 0 <= x、y <= 10^4
// 0 <= z <= 10^7
// 测试链接 : http://poj.org/problem?id=2728
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1001;
const double sml = 1e-6;

int n,x[MAXN],y[MAXN],z[MAXN];
double dist[MAXN][MAXN],cost[MAXN][MAXN],value[MAXN];

bool vis[MAXN];

double prim(double ratio){
    for(int i=1;i<=n;i++){
        vis[i] = false;
        value[i] = cost[1][i] - ratio * dist[1][i];
    }
    vis[1] = true;
    double sum = 0;
    //已经加入了1，所以循环少一次
    for(int i=1;i<=n-1;i++){
        double minVal = 1e18;
        int next = -1;

        //选最小边
        for(int j=1;j<=n;j++){
            if(!vis[j] && value[j] < minVal){
                minVal = value[j];
                next = j;
            }
        }
        sum+=minVal;
        vis[next] = true;
        //更新其他点到生成树最小值
        for(int j=1;j<=n;j++){
            if(!vis[j]){
                double newVal = cost[next][j] - ratio* dist[next][j];
                if(newVal < value[j]){
                    value[j] = newVal;
                }
            }
        }
    }
    return sum;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    while(cin>>n && n){
        for(int i=1;i<=n;i++){
            cin>>x[i]>>y[i]>>z[i];
        }

        //预处理花费
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(i==j) continue;
                double dx = x[i] - x[j];
                double dy = y[i] - y[j];
                dist[i][j] = sqrt(dx*dx + dy*dy);
                cost[i][j] = abs(z[i] - z[j]);
            }
        }
        double l = 0, r = 100;
        while(l+sml<=r){
            double mid = (l+r)/2;
            if(prim(mid)<=0){
                r = mid;
            }else{
                l = mid;
            }
        }
        cout<<fixed<<setprecision(3)<<l<<"\n";
    }
    return 0;
}
