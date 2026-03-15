#include<bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 16;
ll dist(ll x1,ll y1,ll x2,ll y2){
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
}
int cost[MAXN][MAXN];
int dp[1<<MAXN][MAXN],n,cx[MAXN],cy[MAXN];
void build(){
    for(int s=0;s<(1<<n);s++){
        for(int i=0;i<n;i++){
            dp[s][i] = -1;
        }
    }
}
void compute(){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cost[i][j] = dist(cx[i],cy[i],cx[j],cy[j]);
        }
    }
}

int f(int s,int i){
    if(s==(1<<n)-1) return cost[i][0];
    if(dp[s][i]!=-1) return dp[s][i];

    int ans = INT_MAX;
    for(int j=0;j<n;j++){
        if((s>>j&1)==0){
            ans = min(ans,cost[i][j] + f(s|(1<<j),j));
        }
    }
    dp[s][i] = ans;
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n;
    build();
    for(int i=0;i<n;i++){
        cin>>cx[i]>>cy[i];
    }
    compute();
    cout<<f(1,0)<<"\n";
    return 0;
}