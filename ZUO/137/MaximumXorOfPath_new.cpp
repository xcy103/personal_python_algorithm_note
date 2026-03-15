#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 50001;
const int MAXM = 200002;
const int BIT = 60;

int head[MAXN],nxt[MAXM],to[MAXM],cnt;
ll weight[MAXM],path[MAXN],basis[BIT+1];
bool vis[MAXN];

void prepare(int n){
    for(int i=1;i<=n;i++) head[i] = 0;
    memset(basis,0,sizeof(basis));
}

void addEdge(int u,int v,ll w){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt;
}
bool insert_basis(ll num){
    for(int i=BIT;i>=0;i--){
        if((num>>i)&1){
            if(basis[i]==0){
                basis[i] = num;
                return true;
            }
            num^=basis[i];
        }
    }
    return false;
}

void dfs(int u,int fa,ll p){
    path[u] = p;
    vis[u] = true;
    for(int e = head[u];e;e = nxt[e]){
        int v = to[e];
        if(v==fa) continue;
        ll xr = p^weight[e];
        if(vis[v]){
            insert_basis(xr^path[v]);
        }else{
            dfs(v,u,xr);
        }
    }
}
ll query(ll init){
    for(int i=BIT;i>=0;i--){
        init = max(init,init^basis[i]);
    }
    return init;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    prepare(n);

    for(int i=1;i<=m;i++){
        int u,v;
        ll w;
        cin>>u>>v>>w;
        addEdge(u,v,w);
        addEdge(v,u,w);
    }
    dfs(1,0,0);
    cout<<query(path[n])<<"\n";
    return 0;
}