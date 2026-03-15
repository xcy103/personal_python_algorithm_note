#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 20002;
const int BIT = 60;
const int LIMIT = 16;

ll arr[MAXN];
int head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cnt;
int deep[MAXN],stjump[MAXN][LIMIT+1],power;

ll bases[MAXN][BIT+1];
int levels[MAXN][BIT+1];

ll basis[BIT+1];

void addEdge(int u,int v){
    nxt[++cnt] = head[u];
    head[u] = cnt;
    to[cnt] = v;
}
int lg2(int n){
    int ans = 0;
    while((1<<ans)<=(n>>1)) ans++;
    return ans;
}

void prepare(int n){
    memset(head,0,sizeof(head));
    power = lg2(n);
}

bool insertReplace(ll curv,int curl,ll* basis,int* level){
    for(int i=BIT;i>=0;i--){
        if((curv<<i)&1){
            if(basis[i]==0){
                basis[i] = curv;
                level[i] = curl;
                return true;
            }
            if(curl>level[i]){
                swap(curv,basis[i]);
                swap(curl,level[i]);
            }
            curv ^= basis[i];    
        }
    }
    return false;
}

void dfs(int u,int fa){
    deep[u] = deep[fa]+1;
    stjump[u][0] = fa;
    for(int p=1;p<=power;p++){
        stjump[u][p] = stjump[stjump[u][p-1]][p-1];
    }
    for(int i=0;i<=BIT;i++){
        bases[u][i] = bases[fa][i];
        levels[u][i] = levels[u][i];
    }
    insertReplace(arr[u], deep[u], bases[u], levels[u]);

    for(int e = head[u];e;e = nxt[e]){
        int v = to[e];
        if(v!=fa) dfs(v,u);
    }
}
int lca(int a,int b){
    if(deep[a]<deep[b]){
        swap(a,b);
    }
    for(int p=power;p>=0;p--){
        if(deep[stjump[a][p]]>=deep[b]){
            a = stjump[a][p];
        }
    }
    if(a==b) return a;
    for(int p=power;p>=0;p--){
        if(stjump[a][p]!=stjump[b][p]){
            a = stjump[a][p];
            b = stjump[b][p];
        }
    }
    return stjump[a][0];
}
ll query(int x,int y){
    int L = lca(x,y);
    memset(basis,0,sizeof(basis));

    for(int i=BIT;i>=0;i--){
        ll num = bases[x][i];
        if(levels[x][i]>=deep[L] && num!=0){
            basis[i] = num;
        }
    }
    for(int i=BIT;i>=0;i--){
        ll num = bases[y][i];
        if(levels[y][i]>=deep[L] && num){
            for(int j=i;j>=0;j--){
                if((num>>j)&1){
                    if(basis[j]==0){
                        basis[j] = num;
                        break;
                    }
                }
                num^=basis[j];
            }
        }
    }
    ll ans = 0;
    for(int i=BIT;i>=0;i--){
        ans = max(ans,ans^basis[i]);
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,q;
    cin>>n>>q;

    prepare(n);

    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    for(int i=1;i<n;i++){
        int u,v;
        cin>>u>.v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs(1,0);
    while(q--){
        int x,y;
        cin>>x>>y;
        cout<<query(x,y)<<"\n";
    }
    return 0;

}