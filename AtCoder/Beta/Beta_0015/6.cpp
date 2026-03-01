#include<bits/stdc++.h>
using namespace std;
#define ll long long
int h,w,a,b;
int MOD = 1000000007;
int main(){
    
    cin>>h>>w>>a>>b;
    ll dp[h][w];
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            dp[i][j]=0;
        }
    }
    for(int i=0;i<=h-a-1;i++){
        dp[i][0] = 1;
    }
    for(int i=0;i<w;i++){
        dp[0][i] = 1;
    }
    for(int i=1;i<h;i++){
        for(int j=1;j<w;j++){
            if (i>h-a-1 && j<=b-1){
                dp[i][j] = 0;
            }else{
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD;
            }
        }
    }
    cout<<dp[h-1][w-1]<<"\n";
    return 0;
}