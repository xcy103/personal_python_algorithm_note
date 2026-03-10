#include<bits/stdc++.h>
using namespace std;

struct Node{
    int city;
    int power;
    int cost;
    bool operator<(const Node &other) const{
        return cost > other.cost;
    }
};
int electricCarPlan(vector<vector<int>>& paths, int cnt, int start, int end, vector<int>& charge){
    int n = charge.size();

    vector<vector<pair<int, int>>> g(n);
    for(auto& p:paths){
        g[p[0]].push_back({p[1], p[2]});
        g[p[1]].push_back({p[0], p[2]});
    }

    vector<vector<int>> dist(n,vector<int>(cnt+1,INT_MAX));
    vector<vector<bool>> visited(n, vector<bool>(cnt + 1, false));

    priority_queue<Node> pq;
    dist[start][0] = 0;
    pq.push({start, 0, 0});
    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();

        int city = cur.city;
        int power = cur.power;
        int cost = cur.cost;

        if(visited[city][power]) continue;
        if(city == end) return cost;
        visited[city][power] = true;
        if(power < cnt){
            int newCost = cost + charge[city];
            if(!visited[city][power + 1]&& newCost < dist[city][power + 1]){
                dist[city][power + 1] = newCost;
                pq.push({city, power + 1, newCost});
            }
        }
        for(auto& next:g[city]){
            int nextCity = next.first;
            int d = next.second;
            int rest = power - d;
            int nextCost = cost + d;
            if(rest>=0&&!visited[nextCity][rest]&&
            nextCost < dist[nextCity][rest]){
                dist[nextCity][rest] = nextCost;
                pq.push({nextCity, rest, nextCost});
            }
        }
    }
    return -1;
}

