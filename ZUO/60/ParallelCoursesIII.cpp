//拓扑排序拓展，链式前向星建图，就是从入度为0的点
//一次向后退，向后推荐，这里的后指的是，前与后满足一定关系
//https://leetcode.com/problems/parallel-courses-iii/description/
class Solution {
public:
    static const int MAXN = 500002;
    int head[MAXN],nxt[MAXN],to[MAXN],ind[MAXN],cnt;

    void build(){
        cnt = 1;
        for(int i=0;i<MAXN;i++){
            head[i] = nxt[i] = to[i] = ind[i] = 0;
        }
    }
    void add_edge(int u,int v){
        nxt[cnt] = head[u];
        to[cnt] = v;
        head[u] = cnt++;
    }

    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        n = time.size();
        build();

        for(auto& r:relations){
            add_edge(r[0],r[1]);
            ind[r[1]]++;
        }
        queue<int> q;
        vector<int> ans(n,0);
        for(int i=0;i<n;i++){
            if(ind[i+1]==0){
                q.push(i+1);
                ans[i]+=time[i];
            }
        }
        while(!q.empty()){
            int cur = q.front();
            q.pop();

            for(int e=head[cur];e;e = nxt[e]){
                int v = to[e];
                ans[v-1] = max(ans[v-1],ans[cur-1]);
                if(--ind[v]==0){
                    q.push(v);
                    ans[v-1]+=time[v-1];
                }
            }
        }
        return *max_element(ans.begin(), ans.end());
    }
};