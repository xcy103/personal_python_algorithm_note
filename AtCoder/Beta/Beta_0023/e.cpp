#include<bits/stdc++.h>
using namespace std;
using ll = long long; 
const int N = 15;
const ll INF = 10e12;
ll dp[1<<N],cost[1<<N];
int n,c,w[N];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>c;
    for(int i=0;i<n;i++){
        cin>>w[i];
    }
    int mask = 1<<n;
    for(int i=0;i<mask;i++){
        for(int j=0;j<n;j++){
            if((i>>j)&1){
                cost[i]+=w[j];
            }
        }
       
    }
    for(int i=0;i<mask;i++){
        dp[i] = INF;
    }
    dp[0] = 0;
    for(int i=1;i<mask;i++){
        if(cost[i]<=c){
            dp[i] = 1;
            continue;
        }
        int j = i-1;
        while(j>=1){
            dp[i] = min(dp[i],dp[j]+dp[i^j]);
            j = (j-1)&i;
        }
    }
    cout<<dp[(1<<n)-1]<<"\n";
    return 0;
}