#include<bits/stdc++.h>
using namespace std;

struct Edge{
    int u,v,w,i;
};

bool cmp(Edge x,Edge y){
    return x.w > y.w;
}

const int MAXK = 800001;
const int MAXM = 400001;
const int MAXP = 20;

int n,m,q;
Edge edge[MAXM];
int edgeToTree[MAXM],pendEdge[MAXM],pendVal[MAXM];
int cntp;

int f[MAXK],head[MAXK],nxt[MAXK],to[MAXK];
int cntg,nodeKey[MAXK],cntu;
int leafsize[MAXK];
int stjump[MAXK][MAXP];

int find(int x){
    while(x!=f[x]){
        f[x] = f[f[x]];
        x = f[x];
    }
    return f[x];
}
void addEdge(int u,int v){
    nxt[++cntg] = head[u];
    to[cntg] = v;
    head[u] = cntg; 
}

void kruskalRebuild(){
    for(int i=1;i<=n;i++){
        f[i] = i;
    }
    sort(edge+1,edge+m+1,cmp);
    cntu = n;
    for(int i=1,fx,fy;i<=m;i++){
        fx = find(edge[i].u);
        fy = find(edge[i].v);
        if(fx!=fy){
            f[fx] = f[fy] = ++cntu;
            f[cntu] = cntu;
            nodeKey[cntu] = edge[i].w;
            addEdge(cntu,fx);
            addEdge(cntu,fy);
            edgeToTree[edge[i].i] = cntu;
        }
    }
}

void dfs(int u,int fa){
    stjump[u][0] = fa;
    for(int p=1;p<MAXP;p++){
        stjump[u][p] = stjump[stjump[u][p-1]][p-1];
    }
    for (int e = head[u]; e > 0; e = nxt[e]) {
        dfs(to[e], u);
    }
    if(u<=n){
        leafsize[u] = 1;
    }else{
        leafsize[u] = 0;
    }
    for(int e=head[u];e;e = nxt[e]){
        leafsize[u]+=leafsize[to[e]];
    }
}

int query(int u,int limit){
    for(int p = MAXP-1;p>=0;p--){
        if(stjump[u][p] && nodeKey[stjump[u][p]] >= limit){
            u = stjump[u][p];
        }
    }
    return leafsize[u];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m>>q;

    for (int i = 1; i <= m; i++) {
        cin >> edge[i].u >> edge[i].v >> edge[i].w;
        edge[i].i = i;
    }
    kruskalRebuild();
    for(int i=1;i<=cntu;i++){
        if(f[i]==i){
            dfs(i,0);
        }
    }
    int op,x,y,limit = 0;
    for(int i=1;i<=q;i++){
        cin>>op;
        if(op==1){
            for(int k=1;k<=cntp;k++){
                nodeKey[edgeToTree[pendEdge[k]]] = pendVal[k];
            }
            cntp = 0;
            cin>>limit;
        }else if(op==2){
            cin>>x;
            cout << query(x, limit) << "\n";
        }else{
            cin>>x>>y;
            if(edgeToTree[x] != 0){
                pendEdge[++cntp] = x;
                pendVal[cntp] = y;
            }
        }
    }
}
