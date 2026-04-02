/*
Author: yangka
Date: 2026-04-01 16:50:44
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 500001;
const int MAXQ = 2000000001;
using ll  = long long;
// 链式前向星
int head[MAXN], nxt[MAXN<<1], to[MAXN<<1], cnt,weight[MAXN<<1];
int update[MAXN];
ll dist[MAXN];
bool enter[MAXN];
int n,m,q[MAXQ],h,t;
void add_edge(int u,int v,int w){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int cases;
    cin>>cases;
    while(cases--){
        int n,m;
        cin>>n>>m;
        memset(head,0,sizeof(head));
        cnt = 0;
        for(int i=0;i<m;i++){
            int u,v,k;
            cin>>u>>v>>k;
            add_edge(v,u,k);
            add_edge(u,v,-k);
        }
        for(int i=1;i<=n;i++){
            add_edge(0,i,0);
        }
        
    }
    

    return 0;
}