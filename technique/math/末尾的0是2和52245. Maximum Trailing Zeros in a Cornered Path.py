class Solution:
    def maxTrailingZeros(self, g: List[List[int]]) -> int:
        ans = 0
        m,n = len(g),len(g[0])
        mat = [[[0]*2 for _ in range(n+1)] for _ in range(m+1)]
        rows = [[[0]*2 for _ in range(n+1)] for _ in range(m+1)]
        cols = [[[0]*2 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                tmp = g[i][j]
                while tmp%2==0:
                    mat[i+1][j+1][0]+=1
                    tmp//=2
                while tmp%5==0:
                    mat[i+1][j+1][1]+=1
                    tmp//=5
                rows[i+1][j+1][0] = rows[i+1][j][0]+mat[i+1][j+1][0]
                rows[i+1][j+1][1] = rows[i+1][j][1]+mat[i+1][j+1][1]
                cols[i+1][j+1][0] = cols[i][j+1][0]+mat[i+1][j+1][0]
                cols[i+1][j+1][1] = cols[i][j+1][1]+mat[i+1][j+1][1]
        # for i in range(m):
        #     for j in range(1,n+1):
        #         mat[i][j][0]+=mat[i][j-1][0]
        #         mat[i][j][1]+=mat[i][j-1][1]
        # for j in range(n):
        #     for i in range(1,m+1):
        #         mat[i][j][0]+=mat[i-1][j][0]
        #         mat[i][j][1]+=mat[i-1][j][1]
        ans = 0
        for i in range(m):
            for j in range(n):
                p1 = min(rows[i+1][n][0],rows[i+1][n][1])
                p2 = min(cols[m][j+1][0],cols[m][j+1][1])
                x12 = cols[i+1][j+1][0]
                x15 = cols[i+1][j+1][1]

                x22 = rows[i+1][n][0]-rows[i+1][j+1][0]
                x25 = rows[i+1][n][1]-rows[i+1][j+1][1]

                x32 = cols[m][j+1][0] - cols[i][j+1][0]
                x35 = cols[m][j+1][1] - cols[i][j+1][1]#这里写错过

                x42 = rows[i+1][j][0]
                x45 = rows[i+1][j][1]

                p3 = min(x12+x22,x15+x25)
                p4 = min(x22+x32,x25+x35)
                p5 = min(x32+x42,x35+x45)
                p6 = min(x42+x12,x45+x15)
                ans = max(p1,p2,p3,p4,p5,p6,ans)
        return ans

            