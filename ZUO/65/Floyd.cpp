/*
Author: yangka
Date: 2026-03-10 00:21:11
*/
//简单的算法，中间的中转点在最外层枚举

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 101;
const int MAXM = 10001;

int path[MAXM];
int dist[MAXN][MAXN];
int n,m;
ll ans;

void build(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            dist[i][j] = INT_MAX;
        }
    }
}

void floyd(){
    for(int stop = 0; stop < n; stop++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(dist[i][j] > dist[i][stop] + dist[stop][j]){
                    dist[i][j] = dist[i][stop] + dist[stop][j];
                }
            }
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(cin>>n>>m){
        for(int i = 0; i < m; i++){
            cin>>path[i];
            path[i]--;
        }
        build();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin>>dist[i][j];
            }
        }
        floyd();
        for(int i = 1; i < m; i++){
            ans+=dist[path[i-1]][path[i]];
        }
        cout<<ans<<endl;
    }
    
    return 0;
}