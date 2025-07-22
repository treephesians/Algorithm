import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def Backtracking (arr, M):
    if len(arr) == M:
        print(*arr)
    else:
        for i in range(arr[-1] + 1, N + 1):
            new_arr = arr[:]
            new_arr.append(i)
            Backtracking(new_arr, M)

for i in range(1, N + 1):
    arr = [i]
    Backtracking(arr, M)