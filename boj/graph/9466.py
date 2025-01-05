import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(node):
    global result
    visited[node] = 1  # 현재 탐색 중
    cycle.append(node)
    
    next_node = graph[node]
    if visited[next_node] == 0:  # 아직 방문하지 않은 노드
        dfs(next_node)
    elif visited[next_node] == 1:  # 현재 탐색 중인 경로에서 발견한 노드 (사이클 발생)
        cycle_start_index = cycle.index(next_node)
        result += cycle[cycle_start_index:]  # 사이클에 속한 노드 추가

    visited[node] = 2  # 탐색 완료

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)  # 방문 상태 (0: 미방문, 1: 탐색 중, 2: 탐색 완료)
    result = []  # 팀에 속한 학생들

    for i in range(1, n + 1):
        if visited[i] == 0:
            cycle = []  # 현재 탐색 중인 경로
            dfs(i)
    
    # 팀에 속하지 못한 학생 수 출력
    print(n - len(result))