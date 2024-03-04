import sys
from collections import deque

# 입력 대신 변수로 직접 할당
N, K = map(int, sys.stdin.readline().split())

queue = deque([(N, 0)])  # (현재 위치, 이동 횟수)
visited = set([N])  # 방문한 위치 기록

while queue:
    now, cnt = queue.popleft()
    
    if now == K:
        print(cnt)
        break
    
    for next_step in [now - 1, now + 1, now * 2]:
        if 0 <= next_step <= max(N, K) * 2 and next_step not in visited:
            queue.append((next_step, cnt + 1))
            visited.add(next_step)
