#include<bits/stdc++.h>
using namespace std;

const int MAXN = 51;

int dmin[MAXN][MAXN],dmax[MAXN][MAXN];
char s[MAXN][MAXN];

int n,a,b,ans1,ans2,ans3;

void compute(){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(s[i][j]=='='){
                dmin[i][j]=dmax[i][j]=0;
            }else if(s[i][j]=='+'){
                dmin[i][j]=1;
                dmax[i][j]=2;
            }else if(s[i][j]=='-'){
                dmin[i][j]=-2;
                dmax[i][j]=-1;
            }else{
                dmin[i][j]=-2;
                dmax[i][j]=2;
            }
        }
    }

    for(int i=1;i<=n;i++){
        dmin[i][i] = dmax[i][i] = 0;
    }

    for(int k=1;k<=n;k++){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                dmin[i][j] = max(dmin[i][j],dmin[i][k]+dmin[k][j]);
                dmax[i][j] = min(dmax[i][j],dmax[i][k]+dmax[k][j]);
            }

        }
    }
    ans1 = ans2 = ans3 = 0;
    for(int i=1;i<=n;i++){
        for(int j=1;j<i;j++){
            if(i!=a&&i!=b&&j!=a&&j!=b){
                if(dmin[a][i]>dmax[j][b] || dmin[a][j]>dmax[i][b])
                ans1++;
                if(dmax[a][i]<dmin[j][b] || dmax[a][j]<dmin[i][b])
                ans3++;
                if(dmin[a][i]==dmax[a][i]&&dmin[j][b]==dmax[j][b]&&dmin[a][i]==dmin[j][b]){
                    ans2++;
                }else if(dmin[b][i]==dmax[b][i] && dmin[j][a]==dmax[j][a] && dmin[b][i]==dmin[j][a]){
                    ans2++;
                }

            }   
        }
    }
}

int main(){ 
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>a>>b;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>s[i][j];
        }
    }
    compute();
    cout<<ans1<<" "<<ans2<<" "<<ans3<<"\n";
    return 0;
}
