#48
class Solution:

  def rotate(matrix: list[list[int]]) -> None:
    
    n = len(matrix)

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
      for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
      matrix[i].reverse()

#1886
class Solution:
    def findRotation(mat: list[list[int]], target: list[list[int]]) -> bool:
        n=len(mat)
        for i in range(4):
            if mat==target:
                return True
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for row in mat:
                row.reverse()
        return False
    mat=[[0,1],[1,0]]
    target=[[1,0],[0,1]]
    print(findRotation(mat, target))

