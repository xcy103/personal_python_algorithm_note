class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])

        def encode(mat):
            ans = 0

            for i in range(m):
                for j in range(n):
                    if mat[i][j]:
                        ans|=(1<<(i*n+j))
            return ans
        
        start = encode(mat)

        flips = []
        dirs = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                mask = 0
                for dx,dy in dirs:
                    x,y = i+dx,j+dy
                    if 0 <= x < m and 0 <= y < n:
                        mask ^= (1 << (x * n + y))
                flips.append(mask)
        
        q = deque([(start,0)])

        vis = set([start])

        while q:
            s,d = q.popleft()
            if s==0:
                return d
            
            for mask in flips:
                nxt = s ^ mask
                if nxt not in vis:
                    vis.add(nxt)
                    q.append((nxt,d+1))
        return -1