#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 505;
ll mat[MAXN][MAXN];
ll inv[MAXN];

void gauss(int n,int MOD){
    inv[1] = 1;
    for(int i=2;i<MOD;i++){
        inv[i] = (MOD - inv[MOD%i]*(MOD/i)%MOD)%MOD;
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j<i && mat[j][j]!=0) continue;

            if(mat[j][i]!=0){
                for(int k=1;k<=n+1;k++){
                    swap(mat[j][k],mat[i][k]);
                }
                break;
            } 
        }

        if(mat[i][i]==0) continue;

        for(int j=1;j<=n;j++){
            if(i!=j && mat[j][i]){
                ll g = gcd(mat[i][i],mat[j][i]);
                ll a = mat[i][i]/g,b = mat[j][i]/g;

                if(j<i && mat[j][j]){
                    for(int k=j;k<i;k++){
                        mat[j][k] = (mat[j][k]*a)%MOD;
                    }
                }
                for(int k=i;k<=n+1;k++){
                    mat[j][k] = (mat[j][k]*a - mat[i][k]*b + MOD)%MOD;
                }
            }
        }
    }

    for(int i=1;i<=n;i++){
        if(mat[i][i]){
            bool flag = true;
            for(int j=i+1;j<=n;j++){
                if(mat[i][j]){
                    flag = false;
                    break;
                }
            }
            if(flag){
                mat[i][n+1] = (mat[i][n+1]*inv[mat[i][i]])%MOD;
                mat[i][i] = 1;
            }
        }
    }
}