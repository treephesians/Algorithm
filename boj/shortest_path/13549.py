import sys
from collections import deque

input = sys.stdin.readline
max_x = 100001

N, K = map(int, input().split())
dist = [max_x for _ in range(max_x)]
dist[N] = 0

q = deque([N])

while q:
    x = q.popleft()
    d = dist[x]
    if x == K:
        print(d)
        break

    # 0초 걸리는 이동
    nx = x * 2
    if 0 <= nx < max_x and d < dist[nx]:
        dist[nx] = d
        q.appendleft(nx)   # 0초 이동이므로 앞에 추가

    # 1초 걸리는 이동 (x-1)
    nx = x - 1
    if 0 <= nx < max_x and d + 1 < dist[nx]:
        dist[nx] = d + 1
        q.append(nx)       # 1초 이동이므로 뒤에 추가

    # 1초 걸리는 이동 (x+1)
    nx = x + 1
    if 0 <= nx < max_x and d + 1 < dist[nx]:
        dist[nx] = d + 1
        q.append(nx)