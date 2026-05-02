class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[False]*10 for _ in range(9)]
        col = [[False]*10 for _ in range(9)]
        box = [[False]*10 for _ in range(9)]

        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    d = int(board[i][j])
                    row[i][d] = col[j][d] = True
                    box[(i//3)*3 + j//3][d] = True
                else:
                    empty.append((i,j))
        
        def f(pos):
            if pos==len(empty):
                return True
            
            i,j = empty[pos]
            b = (i//3)*3 + j//3

            for d in range(1,10):

                if not row[i][d] and not col[j][d] and not box[b][d]:
                    row[i][d] = col[j][d] = box[b][d] = True
                    board[i][j] = str(d)

                    if f(pos+1):return True

                    row[i][d] = col[j][d] = box[b][d] = False
                    board[i][j] = '.'
            return False
        f(0)
