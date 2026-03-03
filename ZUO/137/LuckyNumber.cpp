#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int MAXN = 20005;
const int BIT = 60;
const int MAXE = MAXN<<1;
int n,q;

// 点权
long long arr[MAXN];
//链式前向星
int head[MAXN];
int nxt[MAXE];
int to[MAXE];
int cnt;
//树上倍增
int LIMIT;
int deep[MAXN];
int stjump[MAXN][20];

//可替换线性基
ll bases[MAXN][BIT+1];
int levels[MAXN][BIT+1];

int log2(int n){
    int ans = 0;
    while((1<<ans)<=(n>>1)) ans+=1;
    return ans;
}

void addEdge(int u,int v){
    nxt[cnt] = head[u];
    to[cnt] = v;
    head[u] = cnt++;
}

bool insertReplace(ll curv,int curl,ll * basis,int* level){
    for(int i=BIT;i>=0;i--){
        if(curv>>i&1LL){
            if(basis[i]==0){
                basis[i] = curv;
                level[i] = curl;
                return true;
            }
        }
        if(curl>level[i]){
            swap(curv,basis[i]);
            swap(curl,level[i]);
        }
        curv^=basis[i];
    }
    return false;
}

void dfs(int u,int f){
    deep[u] = deep[f] + 1;
    stjump[u][0] = f;
    for(int p=1;p<=LIMIT;p++){
        stjump[u][p] = stjump[stjump[u][p-1]][p-1];
    }
    for(int i=0;i<=BIT;i++){
        bases[u][i] = bases[f][i];
        levels[u][i] = levels[f][i];
    }
    insertReplace(arr[u], deep[u], bases[u], levels[u]);

    for(int e=head[u];e;e = nxt[e]){
        int v = to[e];
        if(v!=f){
            dfs(v,u);
        }
    }
}

int lca(int x,int y){
    if(deep[x]<deep[y]) swap(x,y);
    for(int p=LIMIT;p>=0;p--){
        if(deep[stjump[x][p]]>=deep[y]){
            x = stjump[x][p];
        }
    }
    if(x==y) return x;
    for(int p=LIMIT;p>=0;p--){
        if(stjump[x][p]!=stjump[y][p]){
            x = stjump[x][p];
            y = stjump[y][p];
        }
    }
    return stjump[x][0];
}

ll query(int x,int y){
    int l = lca(x,y);
    static long long basis[BIT + 1];
    memset(basis,0,sizeof(basis));

    for(int i=BIT;i>=0;i--){
        if(levels[x][i]>=deep[l]&&bases[x][i]){
            basis[i] = bases[x][i];
        }
    }
    for(int i=BIT;i>=0;i--){
        ll num = bases[y][i];
        if(levels[y][i]>=deep[l]&&num){
            for(int j=i;j>=0;j--){
                if((num>>j)&1LL){
                    if(!basis[j]){
                        basis[j] = num;
                        break;
                    }
                    num^=basis[j];
                }
            }
        }
    }
    ll ans = 0;
    for(int i=BIT;i>=0;i--){
        ans = max(ans,basis[i]^ans);
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,q;
    cin>>n>>q;
    LIMIT = log2(n);
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    for(int i=1;i<n;i++){
        int u,v;
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs(1,0);
    while(q--){
        int u,v;
        cin>>u>>v;
        cout<<query(u,v)<<endl;
    }
    return 0;
}


