/*
Author: yangka
Date: 2026-03-04 21:37:31
*/
// 正整数倍的最小数位和
// 给定一个整数k，求一个k的正整数倍s，使得在十进制下，s的数位累加和最小
// 2 <= k <= 10^5
// 测试链接 : https://www.luogu.com.cn/problem/AT_arc084_b
// 测试链接 : https://atcoder.jp/contests/abc077/tasks/arc084_b
#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using pli = pair<ll,int>;
using minpq = priority_queue<pli, vector<pli>, greater<pli>>;

const int MAXN = 1000005;
const int MAXM = 2000005;
const int MAXK = 100001;
int k;
// 链式前向星
int head[MAXN], nxt[MAXM], to[MAXM], cnt;
int weight[MAXM];
bool vis[MAXK];
deque<pair<int,int>> dq;
void add_edge(int u,int v,double w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}
int bfs(){
    dq.clear();
    dq.push_back({1%k,1});
    while(!dq.empty()){
        auto cur = dq.front();
        dq.pop_front();
        int mod = cur.first;
        int cost = cur.second;

        if(!vis[mod]){
            vis[mod] = true;
            if(mod==0) return cost;
            dq.push_front({(mod*10)%k,cost});
            dq.push_back({(mod+1)%k,cost+1});
        }
    }
    return -1;

}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>k;
    cout<<bfs()<<"\n";

    return 0;
}