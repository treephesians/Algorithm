# https://www.acmicpc.net/problem/15686
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

chicken_house = []
normal_house = []
n_chicken_house = 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 2:
            chicken_house.append([row, col])
            n_chicken_house += 1
        elif matrix[row][col] == 1:
            normal_house.append([row, col])

selected_house = []
visited = [False for _ in range(n_chicken_house)]
distance = 1000

def backtracking(n):
    global distance
    if n == M:
        a = 0
        for nh in normal_house:
            result = 1000
            for sh in selected_house:
                result = min(abs(nh[0] - sh[0]) + abs(nh[1] - sh[1]), result)
            a += result
        distance = min(distance, a)
        return
    for i in range(len(chicken_house)):
        if not visited[i]:
            selected_house.append(chicken_house[i])
            visited[i] = True
            backtracking(n + 1)
            selected_house.pop()
            visited[i] = False

backtracking(0)
print(distance)