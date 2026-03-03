//有三种情况，第一种就是最简单的没有重边的环
//第二种是有重边的环，就是有多个接入点，可以花个图，最后一定被抵消了
//第三种就是有很多简单路径并且有大环
#include<bits/stdc++.h>
using namespace std;
#define ll long long

const int MAXN = 50001;
const int MAXM = 200001;
const int BIT = 60;

int head[MAXN];
int nxt[MAXM<<1], to[MAXM<<1];
ll weight[MAXM<<1];
int cnt;

ll basis[BIT+1];
bool vis[MAXN];
ll path_xor[MAXN];

void prepare(int n){
    cnt = 1;
    for(int i=1;i<=n;i++){
        head[i] = 0;
        vis[i] = false;
    }
    for(int i=0;i<=BIT;i++){
        basis[i] = 0;
    }
}
void addEdge(int u,int v, ll w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}

bool insert(ll num){
    for(int i=BIT;i>=0;i--){
        if((num>>i)&1){
            if(!basis[i]){
                basis[i] = num;
                return true;
            }
            num^=basis[i];
        }
    }
    return false;
}

void dfs(int u,int f, ll xor_sum){
    path_xor[u] = xor_sum;
    vis[u] = true;

    for(int e = head[u];e;e = nxt[e]){
        int v = to[e];
        if(v==f) continue;
        ll cur = xor_sum^weight[e];
        if(vis[v]){
            insert(cur^path_xor[v]);
        }else{
            dfs(v,u,cur);
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
    cout << query(path_xor[n]) << "\n";

    return 0;
}


