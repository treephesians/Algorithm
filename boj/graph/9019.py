# 이 문제의 시간복잡도가 4의 거듭제곱이 아닌 이유는 
# 방문할 수 있는 노드의 개수가 정해져있기 때문이다.
# 이것은 정해진 노드 사이의 최단 거리는 찾는 그래프 문제와 같다.

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def solution(now, end):

    visited = [False for _ in range(10000)]
    visited[now] = True

    dq = deque([(now, [])])

    while dq:
        current, command = dq.popleft()

        if current == end:
            return ''.join(command)

        # case D:
        next_num = (current * 2) % 10000
        if not visited[next_num]:
            visited[next_num] = True
            dq.append((next_num, command + ['D']))

        # case S:
        next_num = 9999 if current == 0 else current - 1
        if not visited[next_num]:
            visited[next_num] = True
            dq.append((next_num, command + ['S']))

        # case L: 4321 
        next_num = (current % 1000) * 10 + (current // 1000)
        if not visited[next_num]:
            visited[next_num] = True
            dq.append((next_num, command + ['L']))

        # case R:
        next_num = (current % 10) * 1000 + (current // 10)
        if not visited[next_num]:
            visited[next_num] = True
            dq.append((next_num, command + ['R']))
    
    return False

answers = []
for _ in range(T):
    current, end = map(int, input().split())
    answers.append(solution(current, end))

print("\n".join(answers))
    