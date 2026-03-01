#include<bits/stdc++.h>
using namespace std;

#define ll long long
const int N = 500001;

int n,m;
ll tree[N];

void add(int i, int v){
    while(i<=n){
        tree[i]+=v;
        i+=(i&-i);
    }
}

ll sum(int i){
    ll ans = 0;
    while(i>0){
        ans+=tree[i];
        i&=(i-1);
    }
    return ans;
}
ll query(int l,int r){
    return sum(r)-sum(l-1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m;

    for(int i = 1;i<=n;i++){
        int v; cin>>v;
        add(i,v);
    }

    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        if(a==1){
            add(b,c);
        }else{
            cout<<query(b,c)<<"\n";
        }
    }
    return 0;
}