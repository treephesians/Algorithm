import sys

N = int(sys.stdin.readline())

cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for rgb in range(3):
        cost[i][rgb] = min(cost[i - 1][(rgb + 1) % 3], cost[i-1][(rgb + 2) % 3]) + cost[i][rgb]
        
print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))