// 外星千足虫
// 一共有n种虫子，编号1~n，虫子腿为奇数认为是外星虫，偶数认为是地球虫
// 一共有m条虫子腿的测量记录，记录编号1~m
// 比如其中一条测量记录为，011 1，表示1号虫没参与，2号、3号虫参与了，总腿数为奇数
// 测量记录保证不会有自相矛盾的情况，但是可能有冗余的测量结果
// 也许拥有从第1号到第k号测量记录就够了，k+1~m号测量记录有或者没有都不影响测量结果
// 打印这个k，并且打印每种虫子到底是外星虫还是地球虫
// 如果使用所有的测量结果，依然无法确定每种虫子的属性，打印"Cannot Determine"
// 1 <= n <= 1000
// 1 <= m <= 2000
// 测试链接 : https://www.luogu.com.cn/problem/P2447
#include<bits/stdc++.h>
using namespace std;

const int MAXN = 2005;
const int MAXS = 2005;

bitset<MAXS> mat[MAXN];

int n,m,s;
int need;

void gauss(int n){
    need = 0;
    for(int i=1;i<=n;i++){
        int povit = -1;
        for(int j=i;j<=n;j++){
            if(mat[j][i])
                povit = j;
                break;
        }
        if(povit == -1){
            return;
        }
        if(povit != i){
            swap(mat[i],mat[povit]);
        }
        need = max(need,povit);
        for(int j=1;j<=n;j++){
            if(j!=i && mat[j][i]){
                mat[j] ^= mat[i];
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m;

    s = max(m,n);

    for(int i=1;i<=m;i++){
        string line;
        cin>>line;
        for(int j=1;j<=n;j++){
            if(line[j-1]=='1'){
                mat[i].set(j);
            }
        }
        int x;
        cin>>x;
        if(x==1){
            mat[i].set(s+1);
        }
    }
    gauss(s);

    for(int i=1;i<=n;i++){
        if(!mat[i][i]){
            cout<<"Cannot Determine"<<"\n";
            return 0;
        }
    }
    cout<<need<<"\n";
    for(int i=1;i<=n;i++){
        if(mat[i][s+1]){
            cout<<"?y7M#"<<"\n";
        }else{
            cout<<"Earth"<<"\n";
        }
    }
    return 0;
}