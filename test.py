import sys

input = sys.stdin.readline

N = int(input())

RGB = [[] for _ in range(N)] 

for i in range(N):
    RGB[i] = list(map(int, input().split()))
    if i == 0 : continue
    for j in range(3):
        RGB[i][j] += min(RGB[i - 1][(j + 1) % 3], RGB[i - 1][(j + 2) % 3])

print(min(RGB[-1]))



