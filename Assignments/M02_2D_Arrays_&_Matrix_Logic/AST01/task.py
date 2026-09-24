#Task
from typing import List
def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]: 
    result = []
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    x, y = rStart, cStart
    step_size = 1
    direction_index = 0

    while len(result) < rows * cols:
        for _ in range(2):  
            for _ in range(step_size):
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                    result.append([x, y])
                    visited.add((x, y))
                x += directions[direction_index][0]
                y += directions[direction_index][1]
            direction_index = (direction_index + 1) % 4  
        step_size += 1  

    return result
   

if __name__ == '__main__':
   rows,cols,rStart,cStart = map(int,input().split())
   print(spiralMatrixIII(rows,cols,rStart,cStart))
