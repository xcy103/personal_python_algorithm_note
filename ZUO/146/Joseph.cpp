
// 约瑟夫环问题
// 一共有1~n这些点，组成首尾相接的环
// 从1号点从数字1开始报数，哪个节点报到数字k，就删除该节点
// 然后下一个节点从数字1开始重新报数，最终环上会剩下一个节点
// 返回该节点的编号
// 1 <= n, k <= 10^6
//首先第一步观察，手撕一个人之后的
//新编号，和老编号之间的关系
//old = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
//new = [7, 8, 9, X, 1, 2, 3, 4, 5, 6]
//发现是 老 = (新 + s(被杀人的编号) - 1)%n(老长度) + 1
//接着找s 和报数k 之间的关系
//这个可以轻松观察出来，是s = (k-1)%n(老长度) + 1
//带入化简可得老 = (新 + k- 1)%n(老长度) + 1
#include<bits/stdc++.h>
using namespace std;

int compute(int n,int k){
    int ans = 1;
    for(int c=2;c<=n;c++){
        ans = (ans + k-1)%c + 1;
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,k;
    cin>>n>>k;
    cout<<compute(n,k)<<"\n";
    return 0;
}