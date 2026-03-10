//这道题就是kruskal算法模板题，但是需要巧妙处理每个节点的花费（点权）
//就是建立一个超级虚拟节点，然后这个虚拟点到这个点的距离（代价）就是
//在这个点打井的花费
class Solution {
public:
    struct Edge{
        int u,v,w;
        bool operator<(const Edge& other) const {
            return w<other.w;
        }
    };
    static const int MAXN = 10010;
    int father[MAXN];
    
    int find(int x){
        while(father[x]!=x){
            father[x] = father[father[x]];
            x = father[x];
        }
        return father[x];
    }
    bool unite(int x, int y){
        int fx = find(x),fy = find(y);
        if(fx!=fy){
            father[fx] = fy;
            return true;
        }
        return false;
    }

    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
        vector<Edge> edges;
        for(int i=0;i<=n;i++){
            father[i] = i;
        }
        for(int i=0;i<n;i++){
            edges.push_back({0, i + 1, wells[i]});
        }
        for(auto& p: pipes){
            edges.push_back({p[0],p[1],p[2]});
        }
        sort(edges.begin(),edges.end());
        int ans = 0;
        for(auto& e:edges){
            if(unite(e.u,e.v)){
                ans+=e.w;
            }
        }
        return ans;
    }
};