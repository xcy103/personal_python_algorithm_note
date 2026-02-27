#include<bits/stdc++.h>
using namespace std;
const int MAXN = 100001;
const int MAXM = 100001;

int head[MAXN];
int nxt[MAXM];
int to[MAXM];
int cnt;

int ind[MAXN];
int ans[MAXN];

int n,m;

void build(int n){
    cnt = 1;
    for(int i=1;i<=n;i++){
        head[i] = 0;
        ind[i] = 0;
    }
}

void addEdge(int u,int v){
    nxt[cnt] = head[u];
    to[cnt] = v;
    head[u] = cnt++;
}

void topoSort(){
    priority_queue<int,vector<int>,greater<int>> pq;

    for(int i=1;i<=n;i++){
        if(ind[i]==0){
            pq.push(i);
        } 
    }

    int fill = 0;

    while(!pq.empty()){
        int cur = pq.top();
        pq.pop();
        ans[fill++] = cur;

        for(int ei = head[cur];ei;ei = nxt[ei]){
            if(--ind[to[ei]]==0){
                pq.push(to[ei]);
            }
        }
    }
}

int main(){ 
    ios::sync_with_stdio(false);
    cin.tie(0);

    while(cin>>n>>m){
        
        build(n);

        int u,v;

        for(int i=0;i<m;i++){
            cin>>u>>v;
            addEdge(u,v);
            ind[v]++;
        }
        topoSort();
    }
}