#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 100001;

ll arr[MAXN],m;
int tree[MAXN<<2],n;

void build(int l,int r,int i){
    if(l==r){
        tree[i] = 1;
        return;
    }else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        tree[i] = tree[i<<1] + tree[i<<1|1];
    }
}
void update(int jobi,int jobv, int l,int r,int i){
    if(l==r){
        tree[i]+= jobv;
        return;
    }else{
        int mid = (l+r)>>1;
        if(jobi<=mid) update(jobi,jobv,l,mid,i<<1);
        else update(jobi,jobv,mid+1,r,i<<1|1);
        tree[i] = tree[i<<1] + tree[i<<1|1];
    }
}

int query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && r<=jobr){
        return tree[i];
    }else{
        int mid = (l+r)>>1;
        int ans = 0;
        if(jobl<=mid) ans += query(jobl,jobr,l,mid,i<<1);
        if(jobr>mid) ans += query(jobl,jobr,mid+1,r,i<<1|1);
        return ans;
    }
}
// 找第k小并删除
int getAndDelete(int k,int l,int r,int i){
    if(l==r){
        tree[i]--;
        return l;
    }else{
        int mid = (l+r)>>1;
        int ans;
        if(tree[i<<1]>=k) ans = getAndDelete(k,l,mid,i<<1);
        else ans = getAndDelete(k-tree[i<<1],mid+1,r,i<<1|1);

        tree[i] = tree[i<<1] + tree[i<<1|1];
        return ans;
    }
}

void compute(){
    build(1,n,1);
    for(int i=1;i<=n;i++){
        int x = arr[i];
        if(x==1) arr[i] = 0;
        else arr[i] = query(1,x-1,1,n,1);
        update(x,-1,1,n,1);
    }
    //这一步求的是有几个数字小于它，
    //我们在线段树里用的是排名
    arr[n]+=m;
    for(int i=n;i>=1;i--){
        arr[i-1]+=arr[i]/(n-i+1);
        arr[i]%=(n-i+1);
    }
    
    build(1,n,1);
    for(int i=1;i<=n;i++){
        arr[i] = getAndDelete(arr[i]+1,1,n,1);
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    compute();
    for(int i=1;i<=n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}