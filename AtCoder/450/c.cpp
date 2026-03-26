#include <bits/stdc++.h>
using namespace std;

int h, w;
vector<string> g;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int i, int j) {
    queue<pair<int,int>> q;
    q.push({i, j});
    g[i][j] = '#';

    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx >= 0 && nx < h && ny >= 0 && ny < w && g[nx][ny] == '.') {
                g[nx][ny] = '#';
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> h >> w;
    g.resize(h);
    for (int i = 0; i < h; i++) {
        cin >> g[i];
    }

    // 1️⃣ 先把边界的 '.' 全部淹掉
    for (int i = 0; i < h; i++) {
        if (g[i][0] == '.') bfs(i, 0);
        if (g[i][w-1] == '.') bfs(i, w-1);
    }
    for (int j = 0; j < w; j++) {
        if (g[0][j] == '.') bfs(0, j);
        if (g[h-1][j] == '.') bfs(h-1, j);
    }

    // 2️⃣ 统计封闭区域
    int ans = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (g[i][j] == '.') {
                ans++;
                bfs(i, j);
            }
        }
    }

    cout << ans << '\n';
    return 0;
}