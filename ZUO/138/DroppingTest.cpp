// 01分数规划模版题
// 给定n个数据，每个数据有(a, b)两个值，都为整数，并且都是非负的
// 请舍弃掉k个数据，希望让剩下数据做到，所有a的和 / 所有b的和，这个比值尽量大
// 如果剩下数据所有b的和为0，认为无意义
// 最后，将该比值 * 100，小数部分四舍五入的整数结果返回
// 1 <= n <= 100
// 0 <= a、b <= 10^9
// 测试链接 : https://www.luogu.com.cn/problem/P10505
// 测试链接 : http://poj.org/problem?id=2976
//分数规划就是，从n个数里面选k个数，使得这些数的比值最大
//
#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
const double eps = 1e-8;

struct Node{
    double a,b,c;
}arr[MAXN];

int n,k;
bool cmp(Node& a, Node& b){
    return a.c > b.c;
}

bool check(double x){
    for(int i=1;i<=n;i++){
        arr[i].c = arr[i].a - x* arr[i].b;
    }
    sort(arr+1, arr+1+n, cmp);
    double sum = 0;
    for(int i=1;i<=k;i++){
        sum += arr[i].c;
    }
    return sum >= 0;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    while(cin>>n>>k){
        if(n==0 && k==0) break;
        k = n-k;
        for(int i=1;i<=n;i++) cin>>arr[i].a;
        for(int i=1;i<=n;i++) cin>>arr[i].b;
        double l = 0, r = 0;
        for(int i=1;i<=n;i++) r += arr[i].a;
        while(l+eps < r){
            double mid = (l+r)/2;
            if(check(mid)) l = mid;
            else r = mid;
        }
        cout << (int)(100 * (l + 0.005)) << "\n";
    }
    return 0;
}