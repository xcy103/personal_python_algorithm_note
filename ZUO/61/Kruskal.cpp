//kruskal算法，不需要建图，最小堆和并查集
//注意这里的边的定义方式
// 时间复杂度O(m * log m) + O(n + m)
#include<bits/stdc++.h>
using namespace std;

const int MAXN = 5001;
const int MAXM = 200001;
int father[MAXN];

struct Edge {
    int u,v,w;
}edges[MAXM];

int n,m;

void build(){
    for(int i=0;i<=n;i++){
        father[i] = i;
    }
}

int find(int x){
    while(father[x]!=x){
        father[x] = father[father[x]];
        x = father[x];
    }
    return father[x];
}

bool unite(int x,int y){
    int fx = find(x),fy = find(y);
    if(fx!=fy){
        father[fx] = fy;
        return true;
    }
    return false;
}

bool cmp(const Edge &a,const Edge &b){
    return a.w<b.w;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m;
    build();

    for(int i=0;i<m;i++){
        cin>>edges[i].u>>edges[i].v>>edges[i].w;
    }
    sort(edges,edges+m,cmp);
    int ans = 0;
    int cnt = 0;
    for(int i=0;i<m;i++){
        if(unite(edges[i].u,edges[i].v)){
            ans += edges[i].w;
            cnt+=1;
        }
    }
    if(cnt==n-1){
        cout<<ans<<endl;
    }else{
        cout<<"orz"<<endl;
    }
    return 0;
    
}
