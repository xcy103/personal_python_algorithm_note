#include<bits/stdc++.h>
using namespace std;

#define ll long long

const int MAXN = 100001;
int tree[MAXN];
int P[MAXN];
int ans[MAXN];
int n,q;

void add(int i, int v){
    while(i <= n){
        tree[i] += v;
        i += i & -i;
    }
}

ll sum(int i){
    ll ans = 0;
    while(i>0){
        ans += tree[i];
        i -= i & -i;
    }
    return ans;
}

ll query(int l, int r){
    return sum(r) - sum(l-1);
}
struct Q{
    int l,r,id;
};

int main(){ 
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> q;
    for(int i=1;i<=n;i++){
        cin>>P[i];
    }
    vector<Q> queries(q);
    for(int i=0;i<q;i++){
        cin>>queries[i].l>>queries[i].r;
        queries[i].id = i;
    }
    sort(queries.begin(),queries.end(),[](Q a,Q b){
        return a.r < b.r;
    });
    unordered_map<int,int> last;
    int cur = 0;

    for(auto& q:queries){
        while(cur<q.r){
            cur++;
            int val = P[cur];
            
            if(last.count(val)){
                add(last[val],-1);
            }
            add(cur,1);
            last[val] = cur;

            ans[q.id] = query(q.r,q.l - 1);
        }

    
    }
    for(int i=0;i<q;i++){
        cout<<ans[i]<<"\n";
    }
    return 0;


}