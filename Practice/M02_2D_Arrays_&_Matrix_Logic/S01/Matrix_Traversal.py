#1572
from typing import List


class Solution:
    def diagonalSum(mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            # Add primary diagonal element
            total_sum += mat[i][i]
            # Add secondary diagonal element
            total_sum += mat[i][n - 1 - i]
            
        # If n is odd, the center element was added twice, so subtract it once
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]
            
        return total_sum
    a=[[1,2,3],[4,5,6],[7,8,9]]
    print(diagonalSum(a))

#498
from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Group elements by the sum of indices (r + c)
        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
                
        result = []
        # Even diagonal sums go upwards (reverse order), odd sums go downwards
        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(reversed(diagonals[d]))
            else:
                result.extend(diagonals[d])
                
        return result
    a=[[1,2,3],[4,5,6],[7,8,9]]
    print((a))
#1380



#1582