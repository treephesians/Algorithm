import sys

input = sys.stdin.readline

N = int(input())
# o o o o
# o o o o
# o o o o
# o o o o
count = 0
col_arr = [True for _ in range(N)]
plus_diagonal = [True for _ in range(2 * N - 1)]
minus_diagonal = [True for _ in range(2 * N - 1)]

def nQueens(row, col, col_arr, plus_diagonal, minus_diagonal):
    global count
    if row == N - 1:
        count += 1
        return
    col_arr[col] = False
    plus_diagonal[row + col] = False
    minus_diagonal[row - col] = False
    for i in range(N):
        if col_arr[i] and plus_diagonal[row + 1 + i] and minus_diagonal[row + 1 - i]:
            nQueens(row + 1, i, col_arr, plus_diagonal, minus_diagonal)
    col_arr[col] = True
    plus_diagonal[row + col] = True
    minus_diagonal[row - col] = True

for col in range(N):
    nQueens(0, col, col_arr, plus_diagonal, minus_diagonal)

print(count)
