import sys
from collections import deque


def find_max_v(start_v, V):
    q = deque([[start_v,0]])
    visited = [[False, 0] for _ in range(V + 1)]
    visited[start_v][0] = True
    max_v = start_v
    max_len = 0
    
    while q:
        now_v, now_len = q.popleft()
        for next in tree[now_v]:
            next_v, next_len = next[0], next[1]
            if not visited[next_v][0]:
                visited[next_v][0] = True
                visited[next_v][1] = now_len + next_len
                q.append([next_v, now_len + next_len])
                if now_len + next_len > max_len:
                    max_v = next_v
                    max_len = now_len + next_len
                    
    return max_v, max_len

V = int(sys.stdin.readline())

tree = [[] for _ in range(V + 1)]


# 트리 만들기
for _ in range(V):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr) - 1, 2):
        tree[arr[0]].append([arr[i], arr[i + 1]])

# 한 점에서 가장 먼 노드 찾기
v, len = find_max_v(1, V)
v2, len2 = find_max_v(v, V)
print(len2)