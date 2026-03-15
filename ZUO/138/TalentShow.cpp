//二分check的时候需要背包判断，判断w的时候，结余是不是非负
#include<bits/stdc++.h>
using namespace std;

const int MAXN = 251;
const int MAXW = 1001;
const double NA = -1e18;
const double sml = 1e-6;

int n,w;
int weight[MAXN],talent[MAXN];
double value[MAXN],dp[MAXW];

bool check(double x){
    for(int i=1;i<=n;i++){
        value[i] = talent[i] - x * weight[i];
    }
    dp[0] = 0;
    for(int i=1;i<=w;i++)dp[i] = NA;
    for(int i=1;i<=n;i++){
        for(int p=w;p>=0;p--){
            int j = p+weight[i];
            if(j>=w){
                dp[w] = max(dp[w],dp[p] + value[i]);
            }else{
                dp[j] = max(dp[j],dp[p] + value[i]);
            }
        }
    }
    return dp[w]>=0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>w;

    for(int i=1;i<=n;i++){
        cin>>weight[i]>>talent[i];
    }

    double l = 0,r = 0;
    for(int i=1;i<=n;i++){
        r+=talent[i];
    }
    double ans = 0;
    while(l+sml<r){
        double mid = (l+r)/2;
        if(check(mid)){
            l=mid;
        }else{
            r=mid;
        }
    }
    cout<<(int)(l*1000)<<"\n";
    return 0;
}