// 工具工厂
// 一共有n种工具，编号1~n，一共有m条记录，其中一条记录格式如下：
// 4 WED SUN 13 18 1 13
// 表示有个工人一共加工了4件工具，从某个星期三开始工作，到某个星期天结束工作
// 加工的工具依次为13号、18号、1号、13号
// 每个工人在工作期间不休息，每件工具都是串行加工的，完成一件后才开始下一件
// 每种工具制作天数是固定的，并且任何工具的制作天数最少3天、最多9天
// 但该数据丢失了，所以现在需要根据记录，推断出每种工具的制作天数
// 如果记录之间存在矛盾，打印"Inconsistent data."
// 如果记录无法确定每种工具的制作天数，打印"Multiple solutions."
// 如果记录能够确定每种工具的制作天数，打印所有结果
// 1 <= n、m <= 300
// 测试链接 : http://poj.org/problem?id=2947
#include<bits/stdc++.h>
using namespace std;

const int MOD = 7;
const int MAXN = 305;

int mat[MAXN][MAXN],inv[MAXN];
string days[7] = {"MON","TUE","WED","THU","FRI","SAT","SUN"};

int day_covert(string s){
    for(int i=0;i<7;i++){
        if(days[i]==s) return i;
    }
    return -1;
}
void build_inverse(){
    inv[1] = 1;
    for(int i=2;i<MOD;i++)
        inv[i] = (MOD - inv[MOD%i] * (MOD/i) % MOD) % MOD;
}

void gauss(int n){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j<i && mat[j][j]) continue;//关键点1，选取所有不是主元的行来比较
            if(mat[j][i]){
                for(int k=1;k<=n+1;k++){
                    swap(mat[j][k],mat[i][k]);
                   
                }
                 break;
            }
        }
        if(mat[i][i]==0) continue;

        for(int j=1;j<=n;j++){
            if(j!=i && mat[j][i]==0) continue;//关键点2，如果这一行相同列为0，不需要消除，直接跳过

            int g = gcd(mat[j][i],mat[i][i]);
            int a = mat[i][i]/g,b = mat[j][i]/g;

            if(j<i && mat[j][j]){//关键点3，如果是在上面的行，需要从头开始，乘
                for(int k=j;k<i;k++){
                    mat[j][k] = (mat[j][k]*a)%MOD;
                }
            }
            for(int k=i;k<=n+1;k++){
                mat[j][k] = ((mat[j][k]*a - mat[i][k]*b)%MOD + MOD)%MOD;
            }
        }
    }
    for(int i=1;i<=n;i++){
        if(mat[i][i]==0) continue;

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

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    build_inverse();

    while(true){
        int n,m;
        cin>>n>>m;

        if(n==0 && m==0) break;

        int s = max(n,m);

        memset(mat,0,sizeof(mat));

        for(int i=1;i<=m;i++){
            int k;
            string sd,ed;

            cin>>k>>sd>>ed;

            for(int j=0;j<k;j++){
                int tool;
                cin>>tool;
                mat[i][tool] = (mat[i][tool] + 1)%MOD;
            }
            mat[i][s+1] = ((day_covert(ed) - day_covert(sd))%MOD+MOD)%MOD;
            
        }

        gauss(s);
        int sign = 1;
        for(int i=1;i<=s;i++){
            if(mat[i][i]==0 && mat[i][s+1]){
                sign = -1;
                break;
            }
            if(i<=n && mat[i][i]==0){
                sign = 0;
            }
        }
        if(sign==-1){
            cout<<"Inconsistent data.\n";
        }
        else if(sign==0){
            cout<<"Multiple solutions.\n";
        }else{
            for(int i=1;i<=n;i++){
                int v = mat[i][s+1];
                if(v<3) v+=7;
                if(i>1) cout<<" ";
                cout<<v;
            }
            cout<<'\n';
        }
    }
    return 0;
}