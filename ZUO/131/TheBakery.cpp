#include<bits/stdc++.h>
using namespace std;

const int MAXN = 350001;

int n,k;
int arr[MAXN];
int dp[MAXN];
int last[MAXN];
int max_tree[MAXN<<2];
int add[MAXN<<2];

void up(int i){
    max_tree[i] = max(max_tree[i<<1],max_tree[i<<1|1]);
}

void lazy(int i,int v){
    max_tree[i]+=v;
    add[i]+=v;
}

void down(int i){
    if(add[i]){
        lazy(i<<1,add[i]);
        lazy(i<<1|1,add[i]);
        add[i] = 0;
    }
}

void build(int l,int r,int i){
    add[i] = 0;
    if(l==r){
        max_tree[i] = dp[l];
        return;
    }
    int mid = (l+r)>>1;
    build(l,mid,i<<1);
    build(mid+1,r,i<<1|1);
    up(i);
}

void rangeAdd(int jobl,int jobr,int jobv,int l,int r,int i){
    if(jobl<=l&&jobr>=r){
        lazy(i,jobv);
        return;
    }
    down(i);
    int mid = (l+r)>>1;
    if(jobl<=mid){
        rangeAdd(jobl,jobr,jobv,l,mid,i<<1);
    }
    if(jobr>mid){
        rangeAdd(jobl,jobr,jobv,mid+1,r,i<<1|1);
    }
    up(i);
}
int rangeQuery(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l&&jobr>=r){
        return max_tree[i];
    }
    down(i);
    int mid = (l + r) >> 1;
    int ans = INT_MIN;
    if (jobl <= mid)
        ans = max(ans, rangeQuery(jobl, jobr, l, mid, i << 1));
    if (jobr > mid)
        ans = max(ans, rangeQuery(jobl, jobr, mid + 1, r, i << 1 | 1));
    return ans;
}

int compute(){
    for(int i=1;i<=n;i++){
        dp[i] = 0;
    }

    for(int t=1;t<=k;t++){
        build(0,n,1);
        memset(last,0,sizeof(int)*(n+1));

        for(int i=1;i<=n;i++){
            rangeAdd(last[arr[i]], i - 1, 1, 0, n, 1);
            if(i>=t){
                dp[i] = rangeQuery(0,i-1,0,n,1);
            }
            last[arr[i]] = i;
        }
        
    }
    return dp[n];

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>k;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    cout<<compute()<<"\n";
    return 0;
}