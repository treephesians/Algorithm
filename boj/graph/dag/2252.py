import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [set() for _ in range(N + 1)]
in_degree_arr = [0 for _ in range(N + 1)]
result_arr = []

for _ in range(M):
    start, end = map(int, input().split())
    in_degree_arr[end] += 1
    arr[start].add(end)

queue = deque([])
for i in range(1, N + 1):
    if in_degree_arr[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    result_arr.append(now)
    for next in arr[now]:
        in_degree_arr[next] -= 1
        if in_degree_arr[next] == 0:
            queue.append(next)

print(*result_arr)

