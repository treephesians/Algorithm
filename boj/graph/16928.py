from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

move_map = {}

for _ in range(N):
    x, y = map(int, input().split())
    move_map[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    move_map[u] = v

visited = [False] * 101
dq = deque([[1, 0]])
visited[1] = True

while dq:
    pos, count = dq.popleft()

    # 사다리 또는 뱀 타기
    if pos in move_map:
        pos = move_map[pos]

    # 도착하면 출력하고 바로 종료
    if pos == 100:
        print(count)
        break

    for i in range(1, 7):
        next_pos = pos + i
        if next_pos <= 100:
            next_pos = move_map.get(next_pos, next_pos)  # 뱀/사다리 반영
            if not visited[next_pos]:
                if next_pos == 100:
                    print(count + 1)
                    sys.exit(0)  # 바로 종료
                visited[next_pos] = True
                dq.append([next_pos, count + 1])