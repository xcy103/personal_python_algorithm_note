class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        m, n = len(g), len(g[0])
        vis = [[False]*n for _ in range(m)]

        def dfs(x, y, px, py, ch):
            if vis[x][y]:
                return True
            
            vis[x][y] = True
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if g[nx][ny] != ch:
                    continue
                if nx == px and ny == py:
                    continue  # ❗不能回头
                
                if dfs(nx, ny, x, y, ch):
                    return True
            
            return False

        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    if dfs(i, j, -1, -1, g[i][j]):
                        return True
        
        return False