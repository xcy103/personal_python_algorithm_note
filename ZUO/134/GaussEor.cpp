/*
Author: yangka
Date: 2026-03-13 15:18:55
*/
//这道题之前让我困惑的一点是，为什么只看自由元怎么选，因为可能有一行有很多自由元
//主元只有一个，选完自由元后，结果只可能有0或者1，所以可以唯一确定主元
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 1000000007;
const int MAXV = 2000;
const int MAXN = 305;

vector<int> prime;
int pow2[MAXN];

void prepare(){
    vector<bool> vis(MAXV+1,false);
    for(int i=2;i<=MAXV;i++){
        if(!vis[i]){
            prime.push_back(i);
            for(int j=i*i;j<=MAXV;j+=i){
                vis[j] = true;
            }
        }
    }
}
int gauss(vector<vector<int>>& mat,int row,int col){
    for(int i=0;i<row;i++){
        for(int j=0;j<row;j++){
            if(j<i&&mat[j][j]) continue;
            if(mat[j][i]){
                swap(mat[i],mat[j]);
                break;
            }
        }
        if(mat[i][i]){
            for(int j=0;j<row;j++){
                if(j!=i && mat[j][i]){
                    for(int k=i;k<col;k++){
                        mat[j][k] ^= mat[i][k];
                    }
                }
            }
        }
        
    }
    int res = 0;
    for(int i=0;i<row;i++){
        if(mat[i][i]) res++;
    }
    return res;
}
ll solve(){


    int n;
    cin>>n;
    vector<ll> arr(n);
    for(int i=0;i<n;i++) cin>>arr[i];
    int cnt = prime.size();
    vector<vector<int>> mat(cnt,vector<int>(n,0));
    
    for(int i=0;i<n;i++){
        ll cur = arr[i];
        for(int j=0;j<cnt;j++){
            ll p = prime[j];
            if(p*p>cur) break;
            while(cur%p==0){
                mat[j][i] ^= 1;
                cur /= p;
            }
        }
    }
    int m = gauss(mat,cnt,n);
    return (pow2[n-m] - 1 + MOD)%MOD;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    prepare();
    pow2[0]=1;
    for(int i=1;i<MAXN;i++) pow2[i]=1LL*pow2[i-1]*2%MOD;
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++){
        cout<<"Case #"<<cs<<":\n";
        cout<<solve()<<"\n";
    }
}