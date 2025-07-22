import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

indexes = [1] * N
for i in range(1, N):
    max_index = 0
    for j in range(0, i):
        if A[i] > A[j]:
            max_index = max(max_index, indexes[j])
        indexes[i] = max_index + 1

print(max(indexes))