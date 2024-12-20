# https://www.acmicpc.net/problem/11404

import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[INF for _ in range(n)] for _ in range(n)] 
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for i in range(n):
    graph[i][i] = 0

for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        answer = graph[i][j]
        e = ' '
        if j == n - 1:
            e = '\n'
        if answer >= INF:
            answer = 0
        print(answer, end = e)