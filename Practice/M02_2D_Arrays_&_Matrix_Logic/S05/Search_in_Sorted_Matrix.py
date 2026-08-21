#sorted matrix problem
#74 
'''
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        arr= []
        for row in matrix:
            arr+=row
        left,right=0,len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if target==arr[mid]:
                return True
            elif target<arr[mid]:
                right=mid-1 
            else:
                left=mid+1
        return False
        
        
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(searchMatrix(matrix,target))
'''
class Solution:
    def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map 1D index 'mid' back to 2D coordinates
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(searchMatrix(matrix,target))
#240
class Solution:
    def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1  # Start at top-right corner
        
        while row < m and col >= 0:
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val > target:
                col -= 1  # Target must be in a smaller column to the left
            else:
                row += 1  # Target must be in a larger row below
                
        return False
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(searchMatrix(matrix,target))


#378
class Solution:
    def kthSmallest(matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        
        # Helper function to count elements <= mid in O(n) time
        def count_less_equal(mid):
            count = 0
            row, col = n - 1, 0  # Start from bottom-left corner
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += (row + 1)  # All elements above in this column are also <= mid
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(kthSmallest(matrix,k))
