#include<bits/stdc++.h>
using namespace std;

const int MAXN = 37;

int mat[MAXN][MAXN],op[MAXN],n,ans;

void prepare(){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            mat[i][j] = 0;
        }
        mat[i][i] = 1;
        mat[i][n+1] = 1;
        op[i] = 0;
    }
}

void swap_row(int a,int b){
    for(int i=1;i<=n+1;i++){
        swap(mat[a][i],mat[b][i]);
    }
}
// XOR 高斯消元
void gauss(int n){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j<i && mat[j][j]) continue;
            if(mat[j][i]){
                swap_row(i,j);
                break;
            }
        }

        if(mat[i][i]){
            for(int j=1;j<=n;j++){
                if(i!=j && mat[j][i]){
                    for(int k=i;k<=n+1;k++){
                        mat[j][k] ^= mat[i][k];
                    }
                }
            }
        }
    }
}

void dfs(int i,int num){
    if(num>=ans) return;

    if(i==0){
        ans = num;
        return;
    }
    if(mat[i][i]==0){
        op[i] = 0;
        dfs(i-1,num);
        op[i] = 1;
        dfs(i-1,num+1);
    }else{
        int cur = mat[i][n+1];
        for(int j=i+1;j<=n;j++){
            if(mat[i][j]) cur^=op[j];
        }
        dfs(i-1,num+cur);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin>>n;
    prepare();

    int m;
    cin>>m;

    for(int i=1;i<=m;i++){
        int u,v;
        cin>>u>>v;
        mat[u][v] = 1;
        mat[v][u] = 1;
    }
    gauss(n);

    bool unique = true;
    for(int i=1;i<=n;i++){
        if(mat[i][i]==0){
            unique = false;
            break;
        }
    }
    if(unique){
        ans = 0;
        for(int i=1;i<=n;i++){
            if(mat[i][n+1]) ans++;
        }
    }else{
        ans = n;
        dfs(n,0);
    }
    cout<<ans<<endl;
}
