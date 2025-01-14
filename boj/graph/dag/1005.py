import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    weight_arr = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    degree = [0] * N

    # 그래프 입력 및 진입 차수 계산
    for _ in range(K):
        start, end = map(int, input().split())
        graph[start - 1].append(end - 1)
        degree[end - 1] += 1

    W = int(input()) - 1

    # 위상 정렬을 위한 큐 초기화
    q = deque()
    dp = [0] * N

    # 진입 차수가 0인 노드를 큐에 추가
    for i in range(N):
        if degree[i] == 0:
            q.append(i)
            dp[i] = weight_arr[i]  # 해당 노드의 가중치로 초기화

    # 위상 정렬 및 DP 수행
    while q:
        current = q.popleft()
        for next_node in graph[current]:
            degree[next_node] -= 1
            # DP 배열 갱신 (최대 가중치 경로 저장)
            dp[next_node] = max(dp[next_node], dp[current] + weight_arr[next_node])
            if degree[next_node] == 0:
                q.append(next_node)

    # 목표 노드 W까지의 최대 가중치 출력
    print(dp[W])