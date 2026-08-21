#54
# class solution:
def spiralOrder(matrix: list[list[int]]) -> list[int]:
        rows,cols=len(matrix),len(matrix[0])
                
        res = []
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        while top <= bottom and left <= right:
            # 1. Move Right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. Move Down
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            if not (top <= bottom and left <= right):
                break
                
            # 3. Move Left
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
            
            # 4. Move Up
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1
            
        return res  
k=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(k))

#59 
class Solution:
    def generateMatrix(n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while num <= n * n:
            # 1. Fill top row (left to right)
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # 2. Fill right column (top to bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # 3. Fill bottom row (right to left)
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # 4. Fill left column (bottom to top)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            
        return matrix
    j=[[1,2,3],[4,5,6],[7,8,9]]
    print(generateMatrix(3))