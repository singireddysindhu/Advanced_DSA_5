#Tasks
def diagonalDifference(arr):
    # Write your code here
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    n = len(arr)
    
    for i in range(n):
        left_diagonal_sum += arr[i][i]
        right_diagonal_sum += arr[i][n - 1 - i]
    
    return abs(left_diagonal_sum - right_diagonal_sum)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)

