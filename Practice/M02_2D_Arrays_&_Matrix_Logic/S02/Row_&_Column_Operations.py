#1351
def countNegatives(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    #count=0
#   for row in grid:
    #   for ele in row:
#           if ele<0:
#               count+=1 
    #return count
    count = 0
    
    row = m - 1
    col = 0
    
    while row >= 0 and col < n:
        if grid[row][col] < 0:
            count += (n - col)
            row -= 1
        else:
            col += 1
    return count
a=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(a))
#832
class Solution:
    def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i]==0:
                    row[i]=1 
                else:
                    row[i]=0
                
        return image
    a=[[1,1,0],[1,0,1],[0,0,0]]
    print(flipAndInvertImage(a))
    
    

   