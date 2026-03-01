#include<bits/stdc++.h>
using namespace std;

static const int MAXN = 10001;
static const int MAXK = 501;
static const int MAXH = 5500;

int n,k;
int arr[MAXN];
int tree[MAXH+1][MAXK+1];

void update(int x, int y, int v){
    for(int i=x;i<=MAXH;i+=i&-i){
        for(int j=y;j<=k+1;j+=j&-j){
            tree[i][j] = max(tree[i][j],v);
        }
    }
}

int query(int x, int y){
    int ans = 0;
    for(int i=x;i>0;i-=i&-i){
        for(int j=y;j>0;j-=j&-j){
            ans = max(ans,tree[i][j]);
        }
    }
    return ans;
}

int compute(){
    int v,dp;
    for(int i=1;i<=n;i++){
        for(int j=k;j>=0;j--){
            v = arr[i] + j;
            dp = query(v,j+1) + 1;
        }
    }
    return query(MAXH,k+1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>k;

    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    cout<<compute()<<"\n";
}
