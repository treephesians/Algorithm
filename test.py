import sys

def is_all_blue(row, col, n, matrix):
    for i in range(n):
        for j in range(n):
            if matrix[row + i][col + j] != 1:
                return 0
    return 1

def is_all_white(row, col, n, matrix):
    for i in range(n):
        for j in range(n):
            if matrix[row + i][col + j] != 0:
                return 0
    return 1

def divide_and_conquer(row, col, n, matrix, n_blue, n_white):
    if is_all_blue(row, col, n, matrix):
        n_blue += 1
    elif is_all_white(row, col, n, matrix):
        n_white += 1
    else:
        # Divide the current square into 4 parts and conquer each
        half_n = n // 2
        n_blue, n_white = divide_and_conquer(row, col, half_n, matrix, n_blue, n_white)
        n_blue, n_white = divide_and_conquer(row, col + half_n, half_n, matrix, n_blue, n_white)
        n_blue, n_white = divide_and_conquer(row + half_n, col, half_n, matrix, n_blue, n_white)
        n_blue, n_white = divide_and_conquer(row + half_n, col + half_n, half_n, matrix, n_blue, n_white)
    return n_blue, n_white

# Assuming N and matrix are given as input in the correct format
# For demonstration, replace the sys.stdin.readline() with some fixed values
# N = int(input())
# matrix = []
# for i in range(N):
#     row = list(map(int, input().split()))
#     matrix.append(row)

n_blue = 0
n_white = 0

# Example input, replace with the actual input mechanism
N = 8
matrix = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
print(matrix)
n_blue, n_white = divide_and_conquer(0, 0, N, matrix, n_blue, n_white)

print(n_white)
print(n_blue)
