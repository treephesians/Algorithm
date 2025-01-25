from collections import deque

def solution(n, edge):
    answer = 0
    matrix = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    
    for a, b in edge:
        matrix[a].append(b)
        matrix[b].append(a)

    q = deque([(1, 0)])
    max_cost = 0

    while q:
        now, cost = q.popleft()
        if not visited[now]:
            visited[now] = True
            if cost > max_cost:
                max_cost = cost
                answer = 0
            answer += 1
            for next in matrix[now]:
                if not visited[next]:
                    q.append((next, cost + 1))

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))