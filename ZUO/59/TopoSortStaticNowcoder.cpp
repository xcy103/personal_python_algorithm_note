#include<bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
const int MAXM = 200001;

int head[MAXN];
int nxt[MAXM];
int to[MAXM];
int cnt;

void build(int n){
    cnt = 1;
    for(int i=1;i<=n;i++){
        head[i] = 0;
    }
}

void addEdge(int u,int v){
    nxt[cnt] = head[u];
    to[cnt] = v;
    head[u] = cnt++;
}

int ind[MAXN];
int q[MAXN];
int ans[MAXN];

bool topoSort(int n){
    int l=0;
    int r=0;
    for(int i=1;i<=n;i++){
        if(ind[i]==0){
            q[r++] = i;
        }
    }
    int fill = 0;
    while (l<r){
        int cur = q[l++];
        ans[fill++] = cur;
        for(int ei = head[cur];ei;ei = nxt[ei]){
            if(--ind[to[ei]]==0){
                q[r++] = to[ei];
            }
        }
    }

    return fill==n;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,m;
    while(cin>>n>>m){
        build(n);
        for(int i=1;i<=n;i++){
            ind[i] = 0;
        }

        int u,v;
        for(int i=0;i<m;i++){
            cin>>u>>v;
            addEdge(u,v);
            ind[v]++;
        }

        if(!topoSort(n)){
            cout<<-1<<"\n";
        }
        else{
            for(int i=0;i<n-1;i++){
                cout<<ans[i]<<" ";
            }
            cout<<ans[n-1]<<"\n";
        }
    }
    return 0;
}