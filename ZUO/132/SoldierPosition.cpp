#include<bits/stdc++.h>
using namespace std;

const int MAXN = 100;
const int MAXM = 10;
const int MAXS = 60;
int n,m,k;
int g[MAXN][MAXM];
int st[MAXS];
int dp[MAXN][MAXS][MAXS];

// 预处理所有合法状态
void prepare(int j,int s){
    if(j>=m){
        st[k++] = s;
    }else{
        prepare(j+1,s);
        prepare(j+3,s|(1<<j));
    }
}

// 统计第 i 行状态 s 能放多少炮兵（结合地形）
int cnt(int i,int s){
    int ans = 0;
    for(int j=0;j<m;j++){
        if((s>>j&1)&&g[i][j]){
            ans++;
        }
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m;

    for(int i=0;i<n;i++){
        string line;
        cin>>line;
        for(int j=0;j<m;j++){
            g[i][j] = (line[j]=='H')?0:1;
        }
    }
    k = 0;
    prepare(0,0);
    memset(dp,0,sizeof(dp));
    
    for(int a=0;a<k;a++){
        dp[0][a][0] = cnt(0,st[a]);
    }
    for(int i=1;i<n;i++){
        for(int a=0;a<k;a++){
            int curCnt = cnt(i,st[a]);
            for(int b=0;b<k;b++){
                if((st[a]&st[b])==0){
                    for(int c=0;c<k;c++){
                        if((st[b]&st[c])==0&&
                            (st[c]&st[a])==0){
                                dp[i][a][b] = max(dp[i][a][b],
                                dp[i-1][b][c] + curCnt);
                            }
                    }
                }
            }
        }
    }
    int ans = 0;
    for(int a=0;a<k;a++){
        for(int b=0;b<k;b++){
            ans = max(ans,dp[n-1][a][b]);
        }
    }
    cout<<ans<<"\n";
    return 0;
}