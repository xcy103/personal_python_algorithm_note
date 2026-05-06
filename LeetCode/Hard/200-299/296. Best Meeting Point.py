#中位数不是平均数
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows = []
        cols = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)

        for c in range(len(grid[0])):
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    cols.append(c)

        row_med = rows[len(rows)//2]
        col_med = cols[len(cols)//2]

        dist = 0

        for r in rows:
            dist += abs(r - row_med)
        for c in cols:
            dist += abs(c - col_med)

        return dist
        