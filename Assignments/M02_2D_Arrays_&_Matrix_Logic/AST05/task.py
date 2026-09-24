from typing import List
def diagonalBoundarySum(arr):
    n = len(arr)
    total_sum = 0

    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1 or i == 0 or i == n - 1 or j == 0 or j == n - 1:
                total_sum += arr[i][j]

    return total_sum

if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    print(diagonalBoundarySum(mat))