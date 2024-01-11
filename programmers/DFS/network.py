def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            stack = [i]
            while stack:
                now = stack.pop()
                if not visited[now]:
                    visited[now] = True
                    for next in range(n):
                        if computers[now][next] == 1 and not visited[next]:
                            stack.append(next)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))