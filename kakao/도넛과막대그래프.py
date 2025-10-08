from collections import defaultdict

def solution(edges):
    edge = defaultdict(list)
    max_node = 0
    answer = [0, 0, 0, 0]
    for start, end in edges:
        edge[start].append(end)
        max_node = max(max_node, start, end)
    
    visited = [False] * (max_node + 1)

    for _, end in edges:
        visited[end] = True

    for i in range(1, max_node + 1):
        if not visited[i] and len(edge[i]) > 1:
            answer[0] = i        
    
    for node in edge[answer[0]]:
        stack = [next for next in edge[node]]
        flag = False
        while stack:
            now = stack.pop()
            if len(edge[now]) == 2:
                flag = True
                answer[3] += 1
                break
            if now == node:
                flag = True
                answer[1] += 1
                break
            
            for next in edge[now]:
                stack.append(next)
        
        if not flag: answer[2] += 1
        
    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edges))