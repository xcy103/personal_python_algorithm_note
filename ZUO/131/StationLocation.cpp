//知识点大杂烩
//补充虚拟村庄，链式前向星，二分
#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int MAXN = 200002;
int n,k;
ll dist[MAXN];
ll fix[MAXN];
ll range[MAXN];
ll warranty[MAXN];

int leftv[MAXN];
int rightv[MAXN];

//链式前向星
int head[MAXN];
int nxt[MAXN];
int to[MAXN];
int cnt;

//线段树
ll int min_tree[MAXN<<2];
ll int add[MAXN<<2];

//dp数组
ll dp[MAXN];

void up(int i){
    min_tree[i] = min(min_tree[i<<1],min_tree[i<<1|1]);

}

void lazy(int i,ll v){
    min_tree[i]+=v;
    add[i]+=v;
}

void down(int i){
    if(add[i]){
        lazy(i<<1,add[i]);
        lazy(i<<1|1,add[i]);
        add[i]=0;
    }
}
void build(int l,int r,int i){
    add[i] = 0;
    if(l==r){
        min_tree[i] = dp[l];
    }else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        up(i);
    }
}

void update(int jobl,int jobr,ll jobv,int l,int r,int i){
    if(jobl<=l&&r<=jobr){
        lazy(i,jobv);
    }
    else{
        down(i);
        int mid = (l+r)>>1;
        if (jobl<=mid){
            update(jobl,jobr,jobv,l,mid,i<<1);
        }
        if (jobr>mid){
            update(jobl,jobr,jobv,mid+1,r,i<<1|1);
        }
        up(i);
    }
}
ll query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l&&r<=jobr){
        return min_tree[i];
    }
    down(i);
    int mid = (l+r)>>1;
    ll ans = LLONG_MAX;
    if (jobl<=mid){
        ans = query(jobl,jobr,l,mid,i<<1);
    }
    if (jobr>mid){
        ans = min(ans,query(jobl,jobr,mid+1,r,i<<1|1));
    }
    return ans;
}

void add_edge(int u,int v){
    nxt[cnt] = head[u];
    to[cnt] = v;
    head[u] = cnt++;
}

int search(ll d){
    int l=0,r = n+1;
    while(l+1<r){
        int mid = (l+r)>>1;
        if(dist[mid]>d){
            r = mid;
        }else{
            l = mid;
        }
    }
    return l;
}
void prepare(){
    cnt = 1;
    memset(head,0,sizeof(head));

    for(int i=1;i<=n;i++){
        leftv[i] = search(dist[i]-range[i]);
        rightv[i] = search(dist[i]+range[i]);

        //如果是最后一个，需要减一下
        if(dist[rightv[i]]>dist[i] + range[i]){
            rightv[i]--;
        }
        add_edge(rightv[i],i);
    }
}
ll compute(){
    ll w = 0;
    for(int i=1;i<=n;i++){
        dp[i] = w+fix[i];
        for(int ei = head[i];ei;ei = nxt[ei]){
            w+=warranty[to[ei]];
        }
    }
    for(int t=2;t<=k+1;t++){
        build(1,n,1);
        for(int i=1;i<=n;i++){
            if(i>=t){
                dp[i] = min(dp[i],
                query(1,i-1,1,n,1)+fix[i]);
            }
            for(int ei = head[i];ei;ei=nxt[ei]){
                int uncover = to[ei];
                if(leftv[uncover]>1){
                    update(1,leftv[uncover]-1,
                    warranty[uncover],1,n,1);
                }
            }
        }
    }
    return dp[n];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>k;
    for(int i=2;i<=n;i++){
        cin>>dist[i];
    }
    for(int i=1;i<=n;i++){
        cin>>fix[i];
    }
    for(int i=1;i<=n;i++){
        cin>>range[i];
    }
    for(int i=1;i<=n;i++){
        cin>>warranty[i];
    }
    dist[++n] = LLONG_MAX;
    fix[n] = range[n] = warranty[n] = 0;
    prepare();
    cout<<compute()<<"\n";

    return 0;
}