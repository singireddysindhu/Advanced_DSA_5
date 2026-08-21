#867 Transpose of a Matrix
#566 Return the transposed matrix
class Solution:
    def transpose(matrix: list[list[int]]) -> list[list[int]]:
        R, C = len(matrix), len(matrix[0])
        # Create an n x m matrix filled with 0s
        transposed = [[0] * R for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                transposed[c][r] = matrix[r][c]
                
        return transposed
    a=[[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(a))
#566
class Solution:
    def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        # Check if reshaping is possible
        if m * n != r * c:
            return mat
        
        # Initialize output matrix
        reshaped = [[0] * c for _ in range(r)]
        
        # Fill output matrix using 1D indexing
        for i in range(m * n):
            reshaped[i // c][i % c] = mat[i // n][i % n]
            
        return reshaped
    a=[[1,2],[3,4]]
    r=1
    c=4
    print(matrixReshape(a, r, c))

