import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

INF = int(1e9)
arr = [INF for _ in range(100001)]
arr[N] = 0
visited = [False for _ in range(100001)]
visited[N] = True

q = deque([N])

while q:
    now = q.popleft()
    if now == K:
        print(arr[now])
        exit()
    if now * 2 <= 100000 and not visited[now * 2]:
        arr[now * 2] = arr[now]
        visited[now * 2] = True
        q.appendleft(now * 2)
    if now - 1 >= 0 and not visited[now - 1]:
        arr[now - 1] = arr[now] + 1
        visited[now - 1] = True
        q.append(now - 1)
    if now + 1 <= 100000 and not visited[now + 1]:
        arr[now + 1] = arr[now] + 1
        visited[now + 1] = True
        q.append(now + 1)