SML = 1e-7

def gauss(mat: list[list[float]], n: int, sml: float = SML) -> None:

    def swap(a,b):
        if a!=b:
            mat[a], mat[b] = mat[b], mat[a]
    
    for i in range(1,n+1):
        max_row = i
        for j in range(1,n+1):
            if j<i and abs(mat[j][i]) >= sml:
                continue
            if abs(mat[j][i]) > abs(mat[max_row][i]):
                max_row = j
        swap(i, max_row)

        if abs(mat[i][i]) >= sml:
            pivot = mat[i][i]

            for col in range(i, n+2):
                mat[i][col] /= pivot
            
            for row in range(1, n+1):
                if row == i:
                    continue
                rate = mat[row][i]
                if abs(rate) < sml:
                    continue
                for col in range(i, n+2):
                    mat[row][col] -= rate * mat[i][col]