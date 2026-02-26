#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e5 + 5;
ll arr[N];
ll sum_tree[N];
ll add_tree[N];

void up(int i){
    sum_tree[i] = sum_tree[i * 2] + sum_tree[i * 2 + 1];
}

void lazy(int i,int v,int n){
    add_tree[i] += v;
    sum_tree[i] += v * n;
}
void build(int l, int r, int i){
    if(l==r){
        sum_tree[i] = arr[l];
        return;
    }
    int mid = (l + r)>>1;
    build(l, mid, i * 2);
    build(mid + 1, r, i * 2 + 1);
    up(i);
}

void down(int i, int ln, int rn){
    if(add_tree[i]){
        lazy(i<<1,ln,add_tree[i]);
        lazy(i<<1|1,rn,add_tree[i]);
        add_tree[i] = 0;
    }
}

void update(int jobl, int jobr, int jobv, int l, int r, int i){
    if(jobl<=l && r<=jobr){
        lazy(i,r-l+1,jobv);
        return;
    }
    int mid = (l + r)>>1;
    down(i,mid-l+1,r-mid);
    if (jobl<=mid) update(jobl,jobr,jobv,l,mid,i<<1);
    if (mid<jobr) update(jobl,jobr,jobv,mid+1,r,i<<1|1);
    up(i);
}

ll query(int jobl, int jobr, int l, int r, int i){
    if(jobl<=l && r<=jobr){
        return sum_tree[i];
    }
    int mid = (l + r)>>1;
    down(i,mid-l+1,r-mid);
    ll ans = 0;
    if (jobl<=mid) ans += query(jobl,jobr,l,mid,i<<1);
    if (mid<jobr) ans += query(jobl,jobr,mid+1,r,i<<1|1);
    return ans;

}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,q;
    cin>>n>>q;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    build(1,n,1);
    while(q--){
        int op;
        cin>>op;
        if(op==1){
            int l,r,v;
            cin>>l>>r>>v;
            update(l,r,v,1,n,1);
        }
        else{
            int l,r;
            cin>>l>>r;
            cout<<query(l,r,1,n,1)<<"\n";
        }
    }
    return 0;
}